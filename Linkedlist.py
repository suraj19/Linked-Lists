class LinkedList:
    class Node:
        def __init__(self,ele):
            self.data=ele
            self.next=None
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def isempty(self):
        return self.count==0
    def addfirst(self,val):
        new_node=self.Node(val)
        if not self.isempty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
    def addlast(self,val):
        new_node=self.Node(val)
        if not self.isempty():
            self.tail.next=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1

    def delFirst(self):
        if not self.is_empty():
            if self.count>1:
                self.head=self.head.next
            else:
                self.head==None
                self.tail=None
            self.count-=1
    def delLast(self):
        if not self.is_empty():
            if self.head==self.tail:
                self.head=self.tail=None
            else:
                tail=self.tail
                cur=self.head
                print("deleting last")
                while(cur.next!=tail):
                    cur=cur.next
                self.tail=cur
                cur.next=None
            self.count-=1
    def countlist(self):
        return self.count
    def maximum(self):
        max=0
        temp=self.head
        while temp:
            if max<int(temp.data):
                max=temp.data
                temp=temp.next
            return max
    def minimum(self):
        min=self.maximum()
        temp=self.head
        while temp:
            if min>temp.data:
                min=temp.data
                temp=temp.next
            return min
    def addAny(self,val,addaftr):
        new_node=self.Node(val)#created object of _Node class, it will have data and next
        if not self.isempty():
            temp=self.head
            while(temp.data!=addaftr and not temp.next is None):
                temp=temp.next
                new_node.next=temp.next
            temp.next=new_node
        else:
            print("mentioned key is not present")
            self.addLast(new_node.data)
        self.count+=1
    def printList(self):
        node=self.head
        while node is not None:
            print(node.data)
            node=node.next
    def delAny(self,val):
        temp1=self.head
        while(temp1.next!=val and not temp1.next is not None):
            temp1=temp1.next
        temp2=temp1.next
        temp1.next=temp2.next
        temp2.next=None
        self.count-=1
#Write a method to reverse the elements in the same list
	def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev