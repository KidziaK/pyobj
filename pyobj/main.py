from typing import Union
from pathlib import Path

from pyobj.c_lib import fast_obj_read, fast_obj_write
from pyobj.mesh import Mesh

def read(path: Union[Path, str]) -> Mesh:
    mesh_p = fast_obj_read(path)
    return Mesh(mesh_p)


def write(mesh: Mesh, path: Union[Path, str]) -> None:
    status = fast_obj_write(mesh.pointer, path)
    if status == 5:
        raise IOError(f"While opening file ({path}) for writing, an exception occured.") 
    elif status != 0:
        raise RuntimeError("Unknown error occurred during OBJ export.")
    

class IOError(Exception):
    pass