from typing import Any, Dict, Union

import numpy as np
import jax.numpy as jnp
from jax import random

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

def nest_for_array(func):
    """Decorator to allow a function to be applied to nested arrays.

    Args:
        func (function): the function to decorate

    Returns:
        function: the decorated function
    """

    def wrapper(arr, *args, **kwargs):
        if isinstance(arr, jnp.ndarray):
            return func(arr, *args, **kwargs)
        elif isinstance(arr, dict):
            if "key_random" in kwargs:
                key_random = kwargs["key_random"]
                del kwargs["key_random"]
                for key, value in arr.items():
                    key_random, subkey = random.split(key_random)
                    arr[key] = wrapper(value, *args, key_random=subkey, **kwargs)
            else:
                for key, value in arr.items():
                    arr[key] = wrapper(value, *args, **kwargs)
            return arr
        elif isinstance(arr, list):
            if "key_random" in kwargs:
                key_random = kwargs["key_random"]
                del kwargs["key_random"]
                for idx, value in enumerate(arr):
                    key_random, subkey = random.split(key_random)
                    arr[idx] = wrapper(value, *args, key_random=subkey, **kwargs)
            else:
                for idx, value in enumerate(arr):
                    arr[idx] = wrapper(value, *args, **kwargs)
            return arr
        else:
            raise ValueError(f"Unknown type for array: {type(arr)}")

    return wrapper


def get_dict_flattened(d, parent_key='', sep='.'):
    """Get a flattened version of a nested dictionary, where keys correspond to the path to the value.

    Args:
        d (Dict): The dictionary to be flattened.
        parent_key (str): The base key string (used in recursive calls).
        sep (str): Separator to use between keys.

    Returns:
        Dict: The flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(get_dict_flattened(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)