from arm.logicnode.arm_nodes import *

class CanvasSetSliderNode(ArmLogicTreeNode):
    """Set canvas text"""
    bl_idname = 'LNCanvasSetSliderNode'
    bl_label = 'Canvas Set Slider'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Element')
        self.add_input('NodeSocketFloat', 'Value')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(CanvasSetSliderNode, category=MODULE_AS_CATEGORY)