import pyobj
from pathlib import Path
import numpy as np

absolute_path = Path(__file__).resolve().parent.joinpath("data/motorbike.obj")
mesh = pyobj.read(absolute_path)

print(mesh.vertices, len(mesh.vertices))
print(mesh.normals, len(mesh.normals))
print(mesh.uvs, len(mesh.uvs))
print(mesh.faces_idx)