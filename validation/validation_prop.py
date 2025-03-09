import bpy
from bpy.types import Scene
from bpy.props import BoolProperty

class TXT_PG_Checker(bpy.types.PropertyGroup):

    value = bpy.props.BoolProperty(name = "value",default = False)

pgclasses = [TXT_PG_Checker]


def register():
    for pgcls in pgclasses:
        bpy.utils.register_class(pgcls)
        Scene.freeze_transform = BoolProperty(name = "Freeze Transform",default=False)

def unregister():
    for pgcls in pgclasses:
        bpy.utils.unregister_class(pgcls)

    del Scene.freeze_transform
