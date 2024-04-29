# research-project-template
A template repository, for the objective of combining research and good code practice.

-   [**Code structure and modularity**](#repository-structure)
-   [**Virtual environment**](#virtual-environment)
-   [**Configuration system (Hydra)**](#configuration-system)
-   [**Logging (tensorboard, WandB, command line)**](#logging)
-   [**Hyperparameter Sweep with WandB**](#hyperparameter-sweep-with-wandb)
-   [**Other tips (macros, ...)**](#other-tips)

# Repository structure
The repository is structured as follows. Each point is detailed below.
```
├── README.md        <- The top-level README for developers using this project
├── configs         <- Configuration files for Hydra. The subtree is detailed below
│ ├─ solver        <- Configuration files for the solver (algorithms? models?, agents?)
│ ├─ task          <- Configuration files for the task (environments?, datasets?)
│ ├─ config_default.yaml  <- Default configuration file
│ └─ personal_config.yaml   <- Your personal configuration file, ignored by git and that you can change as you wish for debugging
├── src             <- Source code for use in this project
├── data            <- Data folder, ignored by git
├── logs           <- Logs folder, ignored by git (tensorboard?, wandb, CSVs, ...)
├── tensorboard    <- Tensorboard logs folder, ignored by git
├── venv           <- Virtual environment folder, ignored by git
├── requirements.txt  <- The requirements file for reproducing the analysis environment
├── LICENSE        <- License file
├── run.py         <- Main script to run the code
└── personal_files <- Personal files, ignored by git (e.g. notes, debugging test scripts, ...)
```

This architecture is based on the fact that any research project requires a configuration, possibly decomposed into several sub-configurations (e.g. solver and task).
The problem that requires to be solved is called a "task" (e.g. dataset, environment, problem, game, etc...) and the method that solves the problem is called a "solver" (e.g. algorithm, model, architecture, agent, etc...). 

The configuration file is used to set the hyperparameters of the running experiment, and to choose the solver and the task, who are themselves defined in sub-configuration files in the `./configs/task/` and `./configs/solver/` folders. Combined with OOP and python interface (with abstract class) methods, this configuration framework allow you to agnostically combine any solver with any task, which allows easily to benchmark different solvers on different tasks.

In this current repository, an example is given with a simple task : minimize the MSE between noise and polynomial functions. There is no training because this is a very proof of concept project, but the code is structured in a way that allows to easily add a training loop.

For the solver, for example, you can easily add a new solver by adding a new file (in the `./solver/` folder advised), implement a class with a `.fit(x_data : np.ndarray)` method, add the mapping between a solver tag and the class in the `./solver/__init__.py` file, and add the configuration file in the `./configs/solver/` folder.

The same goes for the task, and the metrics. This will allow you to easily compare different solvers, tasks, and possibly other things (such as metrics, schedulers, ...), and to easily add new ones, which is an excellent way of doing a research project.

# Virtual environment

For the sake of reproducibility, and to avoid conflicts with other projects, it is recommended to use a virtual environment. 

There are several ways to create a virtual environment. A good one is Virtual Env.

The following commands create a virtual environment named ``./venv/`` and install the requirements.

```bash
python3 -m venv venv
source venv/bin/activate  # for linux
venv\Scripts\activate.bat  # for windows
pip install -r requirements.txt
```

# Configuration system

For a clean way of interacting with the code, it is advised to implement a Command Line Interface (CLI) and a configuration system. A simple approach is to use the ``argparse``, but I suggest to use [Hydra](https://hydra.cc/). Hydra is a framework that allows to easily create a CLI and a configuration system. It is very powerful and flexible, and allows to create a configuration tree.

On this project for example, you can use the following command to run the code with the configuration `_personal_config` in the `configs` folder.

```bash
python run.py --config-name _personal_config
```

Or run the code with the default configuration but with a certain solver on a certain task :

```bash
python run.py solver=linear task=brownian
```

You can also modify config parameters of the configuration file by using the following command :

```bash
python run.py solver=linear task=brownian solver.config.slope=4
```


# Logging 

Logging is a very important part of a project. It allows to keep track of the experiments, to debug, to compare the results, to reproduce the results, etc.

### WandB
WandB is a very powerful tool for logging. It is flexible, logs everything online, can be used to compare experiments or group those by dataset or algorithm, etc. You can also be several people to work on the same project and share the results directly on line. It is also very easy to use, and can be used with a few lines of code.

The metrics will be logged in the project `wandb_config['project']` with entity `wandb_config['entity']`.

Cons : it can sometimes be slow to start. It also makes the CTRL+C command buggy sometimes.

### Tensorboard
Tensorboard is a tool from Tensorflow that allows to visualize the training. It is usefull during the development phase, to check that everything is working as expected. It is also very easy to use, and can be used with a few lines of code.

You can visualize the logs by running the following command in the terminal.
```bash
tensorboard --logdir=tensorboard
```

Cons : it does not log everything online, and it is hard to compare experiments.

### CSV
CSV files are a simple way to log the results. It is good practice to log the results in a CSV file, be it for using the results later.

Cons : it is hard to compare experiments, and it is not very flexible.

# Hyperparameter Sweep with WandB

If you want to perform a hyperparameter sweep, several tools are available, including Optuna, Hydra's sweep and WandB's sweep. Hyperparameter sweeping becomes necessary when the number of hyperparameters becomes too large and/or the intuitive range of values becomes too unknown to be able to manually set them. I present here the WandB sweep, which is very easy to use and very powerful.

You will have to run a wandb command for creating the sweep in the WandB platform, which will give you another WandB command for running the sweep. Here is an example of how to use it.

```bash
wandb sweep usefull_files_for_a_project/sweep.yaml
wandb agent <sweep id given by the previous command>
```

The `sweep.yaml` file is a file that contains the configuration of the sweep. It is a simple file that allows to define the hyperparameters to sweep, the metric to optimize, the number of runs, etc. You can find an example in the `usefull_files_for_a_project/sweep.yaml` file.

A complete documentation can be found [here](https://docs.wandb.ai/guides/sweeps) for how configuring the sweep. Features involve different prior distributions for the hyperparameters, early stopping, etc.

# Other tips

## Macros

Command line macros are extremely useful to avoid typing the same commands over and over again. This is just a small tip that I like to do, but it can save a lot of time.

#### Linux

On Linux, you can create a macro by adding lines in the file ``~/.bashrc``. For example, the following lines create a macro to create the virtual environment and, one to run the code with my personal configuration.

```bash
alias venv="python3 -m venv venv && source venv/bin/activate"
alias run="python run.py --config-name personal_config"
```

#### Windows
On Windows, one method that worked well was to follow this StackOverflow [answer](https://superuser.com/questions/1134368/create-permanent-doskey-in-windows-cmd#:~:text=Create%20a%20file%20to%20store%20your%20macros%20(DOSKEYs).) by the user John DeBord.

Some windows macros that i use can be found in the `usefull_files_for_a_project/macros.doskey` file.

## User-personal usefull files

I advice to use files gitignored (there is a `personal_*` field in the `.gitignore` file) to store personal files, such as notes, debugging scripts, etc. It is a good practice to keep the repository clean and organized.

## cProfile and SnakeViz

cProfile is a module that allows to profile the code. It is very useful to find bottlenecks in the code, and to optimize it. As a developer that wants to optimize the speed of its code, your only criteria for 'how make my code faster' should be how much time the program spend on this function. Note : this is not necessarily the most frequent function.

You can use cProfile by adding the following lines in your code.

```python
import cProfile
with cProfile.Profile() as pr:
    main()  # your code, here it is the main function
pr.print_stats()
pr.dump_stats('logs/profile.prof')
```

SnakeViz is a tool that allows to visualize the results of cProfile and so what you should focus. It is used through the terminal.

```bash
snakeviz logs/profile.prof
```

In development phase, I often create a macro that run the code with my personal config and then run the snakeviz command for visualizing the profiling results.