class Node:
    data: str

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleEndedQueue:
    head: Node
    tail: Node
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

        self.head.next=self.tail

    #*push left, start
    def push_left(self, new_node):
        last_head=self.head
        new_node.next=last_head
        self.head=new_node

    #*push right, end
    def push_right(self, new_node):
        self.tail.next= new_node
        self.tail=new_node

    #*pop left, start
    def pop_left(self):
        self.head=self.head.next

    #*pop right, end
    def pop_right(self):
        current_node = self.head
        last_node= self.head
        next_node = current_node.next

        #Goes through the proccess once, leaving last_node behind by 1
        current_node = next_node
        next_node = current_node.next

        #doesn't go through if next is empty
        while (next_node is not None):
            last_node=last_node.next
            current_node = next_node
            next_node = current_node.next

        self.tail=last_node
        self.tail.next=None


    def print_queue(self):
        current_node=self.head
        num=1
        while current_node is not None:
            print(f"{num}. {current_node.data}")
            current_node=current_node.next
            num+=1

#############################################
node1=Node("Soy el primero")
node2=Node("Soy el último")
stacking=DoubleEndedQueue(node1, node2)
print("2 elementos:")
stacking.print_queue()

stacking.push_left(Node("Soy el segundo"))
stacking.push_right(Node("Soy el tercero"))
stacking.push_right(Node("Soy el cuarto"))
stacking.push_left(Node("Soy el quinto"))
print("\n 5 elementos:")
stacking.print_queue()

stacking.pop_left()
print("\n -Primer elemento:")
stacking.print_queue()

stacking.pop_right()
print("\n -Último elemento:")
stacking.print_queue()