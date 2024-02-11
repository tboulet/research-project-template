from abc import ABC, abstractmethod
from typing import Dict, List

import numpy as np




class BaseSolver(ABC):
    
    def __init__(self, config : Dict):
        self.config_solver = config
        
    @abstractmethod
    def fit(self, x_data : np.ndarray) -> np.ndarray:
        """Example of key methods for the solving process.
        Here as an example we are trying to predict the y data from the x data.
        """