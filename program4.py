#Date: 20-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
'''Modify Q1 such that one can delete any specified element from the list.'''



import Linkedlist

Link=Linkedlist.LinkedList()
'''E1=[x for x in input("enter element in to a list: ").split(',')]
for i in range(len(E1)):
    Link.addfirst(i)
print('Elements in Linked list: ', Link.countlist())
E2=input('Enter element: ')
for i in range(len(E2)):
    Link.addlast(i)
print('Elements in Linked list: ', Link.countlist())'''
Link.addfirst(10)
Link.addlast(20)
Link.addfirst(15)
Link.addlast(25)
Link.printList()
val=input('enter the element you want to delete: ')
Link.delAny(val)
Link.printList()