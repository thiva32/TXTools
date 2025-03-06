import bpy

class TXT_PT_MainPanel(bpy.types.Panel):

    ''' Main Panel for the Addon '''

    bl_idname = "panel.mainpanel"
    bl_label = "TXtool 2025"
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "TXtool 2025"

    def draw(self,context):
    
        layout = self.layout
        box = layout.box()
        row = box.row(align=True)
        
        row.label(text=" v 0.1a ")


from .validation import validation_ui

panels = [TXT_PT_MainPanel]

def register():
    for panel in panels:
        bpy.utils.register_class(panel)
        validation_ui.register()

def unregister():
    for panel in panels:
        bpy.utils.unregister_class(panel)
        validation_ui.unregister()


