from abc import ABC, abstractmethod
from typing import Dict, List

import numpy as np




class BaseSolver(ABC):
    
    def __init__(self, config_solver : Dict):
        self.config_solver = config_solver
        
    @abstractmethod
    def fit(self, x_data : np.ndarray) -> Dict[int, List[int]]:
        """Example of abstract method.
        """