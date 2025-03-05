import bpy


class TXT_OP_FreezeTransform(bpy.types.Operator):

    '''Freeze All Transform'''

    bl_idname ="operator.freezetransform"
    bl_label = "Freeze Transform"

    @classmethod 
    
    def poll(cls,context):
        return context.active_object is not None
    
    def execute(self,context):
        obj = bpy.context.active_object

        location = obj.location
        rotation = obj.rotation_euler
        scale = obj.scale

        if (location != (0,0,0) or rotation != (0,0,0) or scale != (1,1,1)):

            self.report({'INFO'},"Transform Needs to be applied")
            bpy.ops.object.transform_apply(location=True,rotation=True,scale=True) 

        else:
            
            self.report({'INFO'},"Transform Has Been Applied")

        return{'FINISHED'}
    

vld_operator = [TXT_OP_FreezeTransform]

def register():
    for vld_ops in vld_operator:
        bpy.utils.register_class(vld_ops)

def unregister():
    for vld_ops in vld_operator:
        bpy.utils.unregister_class(vld_ops)
