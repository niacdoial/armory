from arm.logicnode.arm_nodes import *

class RemoveTraitNode(ArmLogicTreeNode):
    """Remove trait node"""
    bl_idname = 'LNRemoveTraitNode'
    bl_label = 'Remove Trait'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketShader', 'Trait')
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(RemoveTraitNode, category=MODULE_AS_CATEGORY)