from typing import Any, Dict, Union

import numpy as np


def to_numeric(x: Union[int, float, str, None]) -> Union[int, float]:
    if isinstance(x, int) or isinstance(x, float):
        return x
    elif isinstance(x, str):
        return float(x)
    elif x == "inf":
        return float("inf")
    elif x == "-inf":
        return float("-inf")
    elif x is None:
        return None
    else:
        raise ValueError(f"Cannot convert {x} to numeric")


def try_get_seed(config: Dict) -> int:
    """Will try to extract the seed from the config, or return a random one if not found

    Args:
        config (Dict): the run config

    Returns:
        int: the seed
    """
    try:
        seed = config["seed"]
        if not isinstance(seed, int):
            seed = np.random.randint(0, 1000)
    except KeyError:
        seed = np.random.randint(0, 1000)
    return seed


def try_get(
    dictionnary: Dict, key: str, default: Union[int, float, str, None] = None
) -> Any:
    """Will try to extract the key from the dictionary, or return the default value if not found
    or if the value is None

    Args:
        x (Dict): the dictionary
        key (str): the key to extract
        default (Union[int, float, str, None]): the default value

    Returns:
        Any: the value of the key if found, or the default value if not found
    """
    try:
        return dictionnary[key] if dictionnary[key] is not None else default
    except KeyError:
        return default
