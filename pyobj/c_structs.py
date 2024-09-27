import ctypes

c_float_p = ctypes.POINTER(ctypes.c_float)
c_uint_p = ctypes.POINTER(ctypes.c_uint)

class fastObjIndex(ctypes.Structure):
	_fields_ = [
		("p", ctypes.c_uint),
		("t", ctypes.c_uint),
		("n", ctypes.c_uint),
	]

fastObjIndex_p = ctypes.POINTER(fastObjIndex)


class fastObjTexture(ctypes.Structure):
	_fields_ = [
		("name", ctypes.c_char_p),
		("path", ctypes.c_char_p),
	]

fastObjTexture_p = ctypes.POINTER(fastObjTexture)

class fastObjMaterial(ctypes.Structure):
	_fields_ = [
		("name", ctypes.c_char_p),
		("Ka", ctypes.c_float * 3),
		("Kd", ctypes.c_float * 3),
		("Ks", ctypes.c_float * 3),
		("Ke", ctypes.c_float * 3),
		("Kt", ctypes.c_float * 3),
		("Ns", ctypes.c_float),
		("Ni", ctypes.c_float),
		("Tf", ctypes.c_float * 3),
		("d", ctypes.c_float),
		("illum", ctypes.c_int),
		("fallback", ctypes.c_int),
		("map_Ka", ctypes.c_uint),
		("map_Kd", ctypes.c_uint),
		("map_Ks", ctypes.c_uint),
		("map_Ke", ctypes.c_uint),
		("map_Kt", ctypes.c_uint),
		("map_Ns", ctypes.c_uint),
		("map_Ni", ctypes.c_uint),
		("map_d", ctypes.c_uint),
		("map_bump", ctypes.c_uint),
	]

fastObjMaterial_p = ctypes.POINTER(fastObjMaterial)

class fastObjGroup(ctypes.Structure):
	_fields_ = [
		("name", ctypes.c_char_p),
		("face_count", ctypes.c_uint),
		("face_offset", ctypes.c_uint),
		("index_offset", ctypes.c_uint),
	]

fastObjGroup_p = ctypes.POINTER(fastObjGroup)

class fastObjMesh(ctypes.Structure):
	_fields_ = [
		("position_count", ctypes.c_uint),
		("positions", c_float_p),
		("texcoord_count", ctypes.c_uint),
		("texcoords", c_float_p),
		("normal_count", ctypes.c_uint),
		("normals", c_float_p),
		("color_count", ctypes.c_uint),
		("colors", c_float_p),
		("face_count", ctypes.c_uint),
		("face_vertices", c_uint_p),
		("face_materials", c_uint_p),
		("index_count", ctypes.c_uint),
		("indices", fastObjIndex_p),
		("material_count", ctypes.c_uint),
		("materials", fastObjMaterial_p),
		("texture_count", ctypes.c_uint),
		("textures", fastObjTexture_p),
		("object_count", ctypes.c_uint),
		("objects", fastObjGroup_p),
		("group_count", ctypes.c_uint),
		("groups", fastObjGroup_p),
	]

fastObjMesh_p = ctypes.POINTER(fastObjMesh)