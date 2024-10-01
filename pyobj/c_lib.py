import ctypes
import numpy as np

from sys import platform
from pathlib import Path
from typing import Callable, Type, Union
from pathlib import Path
from collections.abc import Iterable

from .c_structs import *


def __load_lib():
    if platform != "linux":
        error_message = f"Platform {platform} is not supported. Linux is the only supported platform right now."
        raise NotImplementedError(error_message)

    module_path = Path(__file__).resolve().parent
    so_path = module_path.joinpath("lib/libfast_obj_lib.so")

    return ctypes.CDLL(str(so_path))


__lib_fast_obj = __load_lib()


def __get_func(name: str, argtypes: Iterable[Type], restype: Type) -> Callable:
    f = __lib_fast_obj.__getattr__(name)
    f.restype = restype
    f.argtypes = argtypes
    return f


def fast_obj_read(path: Union[str, Path]):
    f = __get_func("fast_obj_read", [ctypes.c_char_p], fastObjMesh_p)
    return f(bytes(str(path), 'ascii'))


def fast_obj_write(mesh, path: Union[str, Path]):
    f = __get_func("fast_obj_write", [fastObjMesh_p, ctypes.c_char_p], ctypes.c_int)
    return f(mesh, bytes(str(path), 'ascii'))
