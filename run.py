# Logging
import wandb
from tensorboardX import SummaryWriter

# Config system
import hydra
from omegaconf import OmegaConf, DictConfig

# Utils
from tqdm import tqdm
import datetime
from time import time
from typing import Dict, Type
import cProfile

# ML libraries
import numpy as np

# Project imports
from folder_tasks import task_name_to_TaskClass
from folder_solvers import solver_name_to_SolverClass
from folder_metrics import metrics_name_to_MetricsClass
from src.time_measure import RuntimeMeter

@hydra.main(config_path="configs", config_name="config_default.yaml")
def main(config : DictConfig):

    # Get the config values from the config object.
    config = OmegaConf.to_container(config, resolve=True)
    algo_name : str = config["algo"]["name"]
    dataset_name : str = config["dataset"]["name"]
    n_iterations : int = config["n_iterations"]
    do_cli : bool = config["do_cli"]
    do_wandb : bool = config["do_wandb"]
    do_tb : bool = config["do_tb"]
    do_tqdm : bool = config["do_tqdm"]
    
    
    
    
    # Get the solver
    SolverClass = solver_name_to_SolverClass[algo_name]
    solver = SolverClass(config = config["algo"]["config"])
    
    # Create the dataset
    TaskClass = task_name_to_TaskClass[dataset_name]
    task = TaskClass(config["dataset"]["config"])
    x_data = task.get_x_data()
    
    # Create the metrics
    metrics = {metric_name : MetricsClass(config["metrics"][metric_name]) for metric_name, MetricsClass in metrics_name_to_MetricsClass.items()}



    # Initialize loggers
    run_name = f"[{algo_name}]_[{dataset_name}]_{datetime.datetime.now().strftime('%dth%mmo_%Hh%Mmin%Ss')}_seed{np.random.randint(1000)}"
    print(f"Starting run {run_name}")
    if do_wandb:
        run = wandb.init(
            name=run_name,
            config=config,
            **config["wandb_config"],
            )
    if do_tb:
        tb_writer = SummaryWriter(log_dir=f"tensorboard/{run_name}")    
    
    # Training loop
    for iteration in tqdm(range(n_iterations), disable=not do_tqdm):
        # Get the clustering result. Measure the time it takes to get the clustering result.
        with RuntimeMeter("solver") as rm:
            clustering_result = solver.fit(x_data=x_data)

        # Log metrics.
        for metric_name, metric in metrics.items():
            with RuntimeMeter("metric") as rm:
                metric_result = metric.compute_metrics(
                    dataset=task, 
                    clustering_result=clustering_result,
                    algo=solver,
                    )
            metric["solver_time"] = rm.get_stage_runtime("solver")
            metric["metric_time"] = rm.get_stage_runtime("metric")
            metric["log_time"] = rm.get_stage_runtime("log")
            metric["iteration"] = iteration
            with RuntimeMeter("log") as rm:
                if do_wandb:
                    cumulative_solver_time_in_ms = int(rm.get_stage_runtime("solver") * 1000)
                    wandb.log(metric_result, step=cumulative_solver_time_in_ms)
                if do_tb:
                    for metric_name, metric_result in metric_result.items():
                        tb_writer.add_scalar(f"metrics/{metric_name}", metric_result, global_step=rm.get_stage_runtime("solver"))
                if do_cli:
                    print(f"Metric results at iteration {iteration} for metric {metric_name}: {metric_result}")

    # Finish the WandB run.
    if do_wandb:
        run.finish()


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        main()
    pr.print_stats()
    pr.dump_stats("logs/profile_stats.prof")
    print("Profile stats dumped to profile_stats.prof")
    print("You can visualize the profile stats using snakeviz by running 'snakeviz logs/profile_stats.prof'")
