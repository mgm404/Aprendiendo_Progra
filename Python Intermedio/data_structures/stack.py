class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    top: Node
    def __init__(self, top):
        self.top = top


    def push(self, new_node):
        last_top=self.top
        new_node.next=last_top
        self.top=new_node


    def pop(self):
        self.top=self.top.next


    def print_stack(self):
        current_node=self.top
        num=1
        while current_node is not None:
            print(f"{num}. {current_node.data}")
            current_node=current_node.next
            num+=1

#############################################
node1=Node("Soy el primero")
stacking=Stack(node1)
print("1 elemento:")
stacking.print_stack()

stacking.push(Node("Soy el segundo"))
stacking.push(Node("Soy el tercero"))
stacking.push(Node("Soy el cuarto"))
stacking.push(Node("Soy el quinto"))
print("\n 5 elementos:") #el primero queda de 5, osea el último
stacking.print_stack()

stacking.pop()
print("\n -1 elementos:") #se quito el quinto, osea el primero en la lista
stacking.print_stack()