from typing import Dict, List

import numpy as np
from folder_solvers.base_solver import BaseSolver


class ConstantSolver(BaseSolver):
    
    def __init__(self, config : Dict):
        super().__init__(config)
        self.value = config["value"]
        
    def fit(self, x_data: np.ndarray) -> Dict[int, List[int]]:
        return self.value * np.ones(x_data.shape[0])
        