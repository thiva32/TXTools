import bpy
import bmesh
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
        

class TXT_OT_NGON(bpy.types.Operator):

    bl_idname = "operator.ngon"
    bl_label = "Ngon"
    bl_options = {'REGISTER','UNDO'}


    def execute(self, context):
        #check if mesh is in edit mode , if not enter edit mode
        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='EDIT')

            #select mesh ngons
            bpy.ops.mesh.select_face_by_sides(number=4 , type='GREATER')
            mesh = bpy.context.active_object.data
            bm = bmesh.from_edit_mesh(mesh)
            total_selected_faces = sum(1 for face in bm.faces if face.select)

            if (total_selected_faces >= 1):
                self.report({'WARNING'},f"Total Ngons : {total_selected_faces}")
            else:
                self.report({'INFO'},f"No Ngons Detected")

        else:
            print("No Object is currently Selected")

        return{'FINISHED'}


        
vld_operator = [TXT_OP_FreezeTransform,TXT_OT_NGON]

def register():
    for vld_ops in vld_operator:
        bpy.utils.register_class(vld_ops)

def unregister():
    for vld_ops in vld_operator:
        bpy.utils.unregister_class(vld_ops)
