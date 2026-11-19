class TreeNode:
    name: str

    def __init__(self, name, left_child=None, right_child=None):
        self.name = name
        self.right_child = right_child
        self.left_child= left_child

class BinaryTree:
    root: TreeNode
    def __init__(self, root):
        self.root = root

    #Código de W3schools, el preOrderTraversal
    #pasa por Root, se va al hijo izquierdo, pasa por la decendencia izquierda y después se va por los dereechos
    def print_tree(self, node):
        if node is None:
            return
        print(node.name, end=", ")
        self.print_tree(node.left_child)
        self.print_tree(node.right_child)



#GEN 5
node14=TreeNode("14")
node15=TreeNode("15")
#GEN 4
node11=TreeNode("11")
node12=TreeNode("12", node14)
node13=TreeNode("13", node15)
#GEN 3
node7=TreeNode("7")
node8=TreeNode("8")
node9=TreeNode("9", node11, node12)
node10=TreeNode("10", node13)
#GEN 2
node5=TreeNode("5")
node6=TreeNode("6", node10)
node3=TreeNode("3", node7, node8)
node4=TreeNode("4", node9)
#GEN 1
node1=TreeNode("1", node3, node4)
node2=TreeNode("2", node5, node6)
#GEN 0
root=TreeNode("Root", node1, node2) 

tree=BinaryTree(root)
tree.print_tree(tree.root)