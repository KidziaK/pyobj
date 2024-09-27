import numpy as np

from typing import Union
from pathlib import Path

from pyobj.c_lib import fast_obj_read, fastObjMesh
from pyobj.mesh import Mesh

def read(path: Union[Path, str]) -> Mesh:
    mesh_p = fast_obj_read(path)
    return Mesh(mesh_p)