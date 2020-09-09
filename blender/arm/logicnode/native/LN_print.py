from arm.logicnode.arm_nodes import *

class PrintNode(ArmLogicTreeNode):
    """Print node"""
    bl_idname = 'LNPrintNode'
    bl_label = 'Print'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'Value')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(PrintNode, category=MODULE_AS_CATEGORY)