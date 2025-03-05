import bpy


class TXT_PT_FreezeTransform(bpy.types.Panel):

    '''Freeze All Transform'''

    bl_idname = "panel.freezetransform"
    bl_label = "Freeze Transform"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TXtool 2025'
    bl_parent_id = 'panel.mainpanel'

    def draw (self,context):

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        row.operator('operator.freezetransform')



vld_panels = [TXT_PT_FreezeTransform]

def register():
    for vld_pnl in vld_panels:
        bpy.utils.register_class(vld_pnl)

def unregister():
    for vld_pnl in vld_panels:
        bpy.utils.unregister_class(vld_pnl)

