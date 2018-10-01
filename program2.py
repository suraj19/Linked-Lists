#Date: 18-09-18
#Author: A.Suraj Kumar
#Roll No: 181046037
#Add methods to Q1 to find maximum and minimum elements in the list.
import Linkedlist

Link=Linkedlist.LinkedList()
E1=input("enter element in to a list: ")
Link.addfirst(E1)
print('Elements in Linked list: ', Link.countlist())
E2=input('Enter element: ')
Link.addlast(E2)
print('Elements in Linked list: ', Link.countlist())
Link.maximum()
#print('Maximum Element in a List: ',)