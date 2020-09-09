from arm.logicnode.arm_nodes import *

class ShutdownNode(ArmLogicTreeNode):
    """Shutdown node"""
    bl_idname = 'LNShutdownNode'
    bl_label = 'Shutdown'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(ShutdownNode, category=MODULE_AS_CATEGORY)