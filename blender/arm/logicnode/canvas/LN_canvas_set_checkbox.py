from arm.logicnode.arm_nodes import *

class CanvasSetCheckBoxNode(ArmLogicTreeNode):
    """Set canvas check box"""
    bl_idname = 'LNCanvasSetCheckBoxNode'
    bl_label = 'Canvas Set Checkbox'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Element')
        self.add_input('NodeSocketBool', 'Value')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(CanvasSetCheckBoxNode, category=MODULE_AS_CATEGORY)