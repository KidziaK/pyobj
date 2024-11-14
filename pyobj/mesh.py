import ctypes
import numpy as np

from .c_structs import *

class Mesh:
    def __init__(self, mesh_ptr: fastObjMesh_p) -> None:
        self.__fastObjMesh = mesh_ptr.contents

    @property
    def pointer(self) -> fastObjMesh_p:
        return self.__fastObjMesh

    def __get_buffer(self, buf_name: str, count_name: str, buffer_dims: int = 1) -> np.ndarray:
        mesh = self.__fastObjMesh
        count = getattr(mesh, count_name)
        buffer = getattr(mesh, buf_name)
        shape = (count,) if buffer_dims == 1 else (count, buffer_dims)
        return np.ctypeslib.as_array(buffer, shape=shape)

    @property
    def vertices(self) -> np.ndarray:
        return self.__get_buffer("positions", "position_count", 3)

    @vertices.setter
    def vertices(self, value: np.ndarray) -> None:
        mesh = self.__fastObjMesh
        mesh.positions = value.data
        mesh.position_count = len(value)

    @property
    def normals(self) -> np.ndarray:
        return self.__get_buffer("normals", "normal_count", 3)

    @property
    def uvs(self) -> np.ndarray:
        return self.__get_buffer("texcoords", "texcoord_count", 2)

    @property
    def faces(self) -> np.ndarray:
        return self.__get_buffer("face_vertices", "face_count")

    @property
    def faces_idx(self) -> np.ndarray:
        # face[i] = list of (vertex, uv, normal)
        return self.__get_buffer("indices", "index_count")
