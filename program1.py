#Date: 18-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
'''Create a single list with methods to add and delete elements from head and tail positions. 
Provide method to check whether an element is present in the list. Count number of elements in the list.'''

import Linkedlist

Link=Linkedlist.LinkedList()
E1=input("enter element in to a list: ")
Link.addfirst(E1)
print('Elements in Linked list: ', Link.countlist())
E2=input('Enter element: ')
Link.addlast(E2)
print('Elements in Linked list: ', Link.countlist())
Link.delFirst()
print('count of elements in list',Link.countlist())
Link.delLast()
print('count of elements in list',Link.countlist())