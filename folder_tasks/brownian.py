

import numpy as np
from folder_tasks.base_dataset import BaseTask


class BrownianTask(BaseTask):
    
    def __init__(self, config) -> None:
        super().__init__(config)
        B0 = [0]
        for i in range(1, 100):
            B0 = B0 + [B0[-1] + np.random.normal()]
        self.B_t = np.array(B0)
        
    def get_x_data(self):
        return self.B_t
    
    def get_labels(self) -> np.ndarray:
        return self.B_t