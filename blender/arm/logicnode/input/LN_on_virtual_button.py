from arm.logicnode.arm_nodes import *

class OnVirtualButtonNode(ArmLogicTreeNode):
    """On virtual button node"""
    bl_idname = 'LNOnVirtualButtonNode'
    bl_label = 'On Virtual Button'
    property0: EnumProperty(
        items = [('Down', 'Down', 'Down'),
                 ('Started', 'Started', 'Started'),
                 ('Released', 'Released', 'Released')],
        name='', default='Started')
    property1: StringProperty(name='', default='button')

    def init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
        layout.prop(self, 'property1')

add_node(OnVirtualButtonNode, category=MODULE_AS_CATEGORY, section='virtual')