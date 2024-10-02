#include <stdio.h>
#include "fast_obj.h"

int fast_obj_write(fastObjMesh* mesh, const char* path)
{
    FILE *fout;

    if (!(fout = fopen(path, "w")))
    {
        printf("Error - couldn't open file for writing (path: %s)", path);
        return 5;
    }

    // Write all positions
    for (unsigned int pi = 1; pi < mesh->position_count; ++pi)
    {
        fprintf(fout, "v %f %f %f\n", 
                        mesh->positions[pi*3], mesh->positions[pi*3+1], mesh->positions[pi*3+2]);   
    }

    // Write all tex coords
    for (unsigned int ti = 1; ti < mesh->texcoord_count; ++ti)
    {
        fprintf(fout, "vt %f %f\n", 
                        mesh->texcoords[ti*2], mesh->texcoords[ti*2+1]);   
    }

    // Write all normals
    for (unsigned int ni = 1; ni < mesh->normal_count; ++ni)
    {
        fprintf(fout, "vn %f %f %f\n", 
                        mesh->normals[ni*3], mesh->normals[ni*3+1], mesh->normals[ni*3+2]);   
    }

    // For every object in the structure...
    for (unsigned int oi = 0; oi < mesh->object_count; ++oi)
    {
        fprintf(fout, "o %s\n", mesh->objects[oi].name);
        unsigned int ii = mesh->objects[oi].index_offset;
        // ...write all faces
        for (unsigned int fi = 0; fi < mesh->objects[oi].face_count; ++fi)
        {
            fprintf(fout, "f ");
            // We have to go through all vertices to write them in file
            for (unsigned int vi = 0; vi < mesh->face_vertices[fi + mesh->objects[oi].face_offset]; ++vi)
            {
                // If t == 0, then tex coords are undefined and we can skip them
                if(mesh->indices[ii].t == 0)
                    fprintf(fout, "%d//%d ", mesh->indices[ii].p, mesh->indices[ii].n);
                else
                    fprintf(fout, "%d/%d/%d ", mesh->indices[ii].p, mesh->indices[ii].t, mesh->indices[ii].n);
                ii++;
            }

            fprintf(fout, "\n");
        }
    }

    fclose(fout);
    return 0;
}