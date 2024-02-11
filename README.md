# research-project-template
A template repository, for the objective of combining research and good code practice. It focuses on code structure, modularity, configuration system (Hydra) and logging (tensorboard and WandB)

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

# Configuration system : Hydra

For a clean way of interacting with the code, it is advised to implement a Command Line Interface (CLI) and a configuration system. A simple approach is to use the ``argparse``, but I suggest to use [Hydra](https://hydra.cc/). Hydra is a framework that allows to easily create a CLI and a configuration system. It is very powerful and flexible, and allows to create a configuration tree.

On this project for example, you can use the following command to run the code with the configuration `personal_config` in the `configs` folder.

```bash
python run.py --config-name personal_config
```

Or run the code with the default configuration but with a certain solver on a certain task :

```bash
python run.py solver=linear task=brownian
```

You can also modify config parameters of the configuration file by using the following command :

```bash
python run.py solver=linear task=brownian solver.lr=0.01
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

# Macros

Command line macros are extremely useful to avoid typing the same commands over and over again. 

#### Linux

On Linux, you can create a macro by adding lines in the file ``~/.bashrc``. For example, the following lines create a macro to create the virtual environment and, one to run the code with my personal configuration.

```bash
alias venv="python3 -m venv venv && source venv/bin/activate"
alias run="python run.py --config-name personal_config"
```

#### Windows
On Windows, one method that worked well was to follow this StackOverflow [answer](https://superuser.com/questions/1134368/create-permanent-doskey-in-windows-cmd#:~:text=Create%20a%20file%20to%20store%20your%20macros%20(DOSKEYs).) by the user John DeBord.

Some windows macros that i use can be found in the `usefull_files_for_a_project/macros.doskey` file.

# Personal files

I advice to use files gitignored (there is a `personal_*` field in the `.gitignore` file) to store personal files, such as notes, debugging scripts, etc. It is a good practice to keep the repository clean and organized.