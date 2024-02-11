

import numpy as np
from folder_tasks.base_dataset import BaseTask


class WhiteNoiseTask(BaseTask):
    
    def __init__(self, config) -> None:
        super().__init__(config)
        self.B_t = np.random.normal(size=100)
        
    def get_x_data(self):
        return self.B_t
    
    def get_labels(self) -> np.ndarray:
        return self.B_t