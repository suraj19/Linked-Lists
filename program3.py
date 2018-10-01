#Date: 19-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
'''Modify Q1 such that one can add a new element after any specified element.'''
import Linkedlist

Link=Linkedlist.LinkedList()
E1=input("Enter an element to be added in a head of list: ")
Link.addfirst(E1)
print('Elements in Linked list: ', Link.countlist())
E2=input('Enter an element to be added in a tail of list: ')
Link.addlast(E2)
print('Elements in Linked list: ', Link.countlist())
add=input("enter a new element to be added in a list: ")
after=input('enter the element you want to add after: ')
Link.addAny(add,after)
Link.printList()