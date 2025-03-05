import bpy

class TXT_PT_MainPanel(bpy.types.Panel):
    ''' Main Panel for the Addon '''
    bl_idname = "TXT_PT_mainpanel"
    bl_label = "TXtool 2025"
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "TXtool 2025"

    def draw(self,context):
    
        layout = self.layout
        row = layout.row()

        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        
        row.label(text=" v 0.1a ")




panels = [TXT_PT_MainPanel]

def register():
    for panel in panels:
        bpy.utils.register_class(panel)

def uregister():
    for panel in panels:
        bpy.utils.uregister_class(panel)


