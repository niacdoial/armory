from arm.logicnode.arm_nodes import *

class CanvasGetSliderNode(ArmLogicTreeNode):
    """Set canvas text"""
    bl_idname = 'LNCanvasGetSliderNode'
    bl_label = 'Canvas Get Slider'

    def init(self, context):
        self.add_input('NodeSocketString', 'Element')
        self.add_output('NodeSocketFloat', 'Value')

add_node(CanvasGetSliderNode, category=MODULE_AS_CATEGORY)