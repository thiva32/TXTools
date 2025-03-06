import bpy


class TXT_PT_CleanupTools(bpy.types.Panel):

    '''Freeze All Transform'''

    bl_idname = "panel.cleanuptools"
    bl_label = "Cleanup Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'TXtool 2025'
    bl_parent_id = 'panel.mainpanel'
    bl_context = 'OBJECT'

    def draw (self,context):

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        #Freeze transform operator button
        row.operator('operator.freezetransform')


#classes to register 
vld_panels = [TXT_PT_CleanupTools]


def register():
    for vld_pnl in vld_panels:
        bpy.utils.register_class(vld_pnl)

def unregister():
    for vld_pnl in vld_panels:
        bpy.utils.unregister_class(vld_pnl)

