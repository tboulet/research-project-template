from typing import Dict, Type
from folder_metrics.base_metric import BaseMetric
from folder_metrics.mse import MeanSquaredError


metrics_name_to_MetricsClass : Dict[str, Type[BaseMetric]] = {
    "mse" : MeanSquaredError
}