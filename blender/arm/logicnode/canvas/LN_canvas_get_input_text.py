from arm.logicnode.arm_nodes import *

class CanvasGetInputTextNode(ArmLogicTreeNode):
    """Get canvas input text"""
    bl_idname = 'LNCanvasGetInputTextNode'
    bl_label = 'Canvas Get Input Text'

    def init(self, context):
        self.add_input('NodeSocketString', 'Element')
        self.add_output('NodeSocketString', 'Value')

add_node(CanvasGetInputTextNode, category=MODULE_AS_CATEGORY)