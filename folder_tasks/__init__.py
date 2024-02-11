from typing import Dict, Type
from folder_tasks.base_dataset import BaseTask
from folder_tasks.brownian import BrownianTask
from folder_tasks.white_noise import WhiteNoiseTask


task_name_to_TaskClass : Dict[str, Type[BaseTask]] = {
    "brownian" : BrownianTask,
    "white_noise" : WhiteNoiseTask,
}