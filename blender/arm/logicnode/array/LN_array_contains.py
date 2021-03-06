from arm.logicnode.arm_nodes import *

class ArrayContainsNode(ArmLogicTreeNode):
    """Returns whether the given array contains the given value."""
    bl_idname = 'LNArrayInArrayNode'
    bl_label = 'Array Contains'
    arm_version = 1

    def init(self, context):
        super(ArrayContainsNode, self).init(context)
        self.add_input('ArmNodeSocketArray', 'Array')
        self.add_input('NodeSocketShader', 'Value')
        self.add_output('NodeSocketBool', 'Contains')
