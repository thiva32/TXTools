import bpy
from mathutils import Vector

def freezetransform_func(context):

    obj = bpy.context.active_object
        
    location = obj.location
    rotation = obj.rotation_euler
    scale = obj.scale

    if (location == Vector((0.0,0.0,0.0)) and rotation == Euler((0.0,0.0,0.0)) and scale == Vector((1.0,1.0,1.0))):
        print("Transform is good")     
    else:
        bpy.ops.object.transform_apply(location=True,rotation=True,scale=True) 
        print("Transform Has Been Applied")  

        