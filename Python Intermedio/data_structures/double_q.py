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
        if self.head.next == None:
            self.head.next=new_node
            self.tail=new_node
            
        else:
            self.tail.next= new_node #makes old tail point to new node
            self.tail=new_node #makes new node the tail

    #*pop left, start
    def pop_left(self):
        self.head=self.head.next #Takes out the head, nothing points to the eliminated value, because its the HEAD

    #*pop right, end
    def pop_right(self):
        current_node = self.head
        last_node= self.head
        next_node = current_node.next

        #Goes through the proccess once, leaving last_node behind by 1
        if next_node is not None:
            current_node = next_node
            next_node = current_node.next
        else:
            return

        #doesn't go through if next is empty
        while (next_node is not None):
            last_node=last_node.next
            current_node = next_node
            next_node = current_node.next

        self.tail=last_node
        self.tail.next=None #takes out the old tail by making the new one point to nothing


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