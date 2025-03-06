import bpy
from mathutils import Vector,Euler

#This operator checks for the current transform of the mesh .
#if the transform is frozen/applied it will skip and just print info
#if location is not equal to 0 , scale not equal to 1 or rotation not equal to 0
#it will apply the transform

class TXT_OP_FreezeTransform(bpy.types.Operator):

    '''Freeze All Transform'''

    bl_idname ="operator.freezetransform"
    bl_label = "Freeze Transform"
    bl_options = {'REGISTER','UNDO'}

    @classmethod 
    def poll(cls,context):
        #This makes sure objects are selected
        return context.active_object is not None
    
    def execute(self,context):

        obj = bpy.context.active_object
        
        location = obj.location
        rotation = obj.rotation_euler
        scale = obj.scale

        if (location == Vector((0.0,0.0,0.0)) and rotation == Euler((0.0,0.0,0.0)) and scale == Vector((1.0,1.0,1.0))):
            self.report({'INFO'},"Transform is good")     
        else:
            bpy.ops.object.transform_apply(location=True,rotation=True,scale=True) 
            self.report({'INFO'},"Transform Has Been Applied")  

        return{'FINISHED'}
        
        

vld_operator = [TXT_OP_FreezeTransform]

def register():
    for vld_ops in vld_operator:
        bpy.utils.register_class(vld_ops)

def unregister():
    for vld_ops in vld_operator:
        bpy.utils.unregister_class(vld_ops)
