from abc import ABC, abstractmethod
from typing import Dict, List

from folder_solvers.base_solver import BaseSolver


class BaseMetric(ABC):
        
    @abstractmethod
    def compute_metrics(self, 
                        dataset, 
                        clustering_result : Dict[int, List[int]],
                        algo : BaseSolver,
                        ) -> Dict[str, float]:
        """Example of abstract method for computing metrics.
        """