

from typing import Dict, List

import numpy as np
from folder_metrics.base_metric import BaseMetric
from folder_solvers.base_solver import BaseSolver
from folder_tasks.base_dataset import BaseTask


class MeanSquaredError(BaseMetric):
    
    def compute_metrics(self, 
            task : BaseTask,
            y_pred: np.ndarray,
            algo: BaseSolver,
        ) -> Dict[str, float]:
        y_data = task.get_labels()
        return {"mse" : ((y_data - y_pred) ** 2).mean()}