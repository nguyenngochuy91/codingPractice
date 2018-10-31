#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:40:32 2018

@author: huyn
"""
try:
    from queue import Queue as q
except:
    from multiprocessing import Queue as q
# given n nodes, and edges, find the number of connected components

def bfsConnectedComponents(n,edges):
    neighbors = {}
    visited = set()
    for i in range(n):
        neighbors[i] = []
    for e in edges:
        node1 = e[0]
        node2 = e[1]
        neighbors[node1].append(node2)
        neighbors[node2].append(node1)
    connected = []

    while neighbors:
        newConnectedComponent= []
        item = neighbors.popitem()
        currentNode = item[0]
        visited.add(currentNode)
        newConnectedComponent.append(currentNode)
        currentNeighbors = item[1]
        nextNeighbors  = []
        while currentNeighbors:
            neighbor = currentNeighbors.pop(-1)
            if neighbor not in visited:
                newConnectedComponent.append(neighbor)
                visited.add(neighbor)
                moreNeighbors = neighbors.pop(neighbor)
                for m in moreNeighbors:
                    if m not in visited:
                        nextNeighbors.append(m)
            if not currentNeighbors:
                currentNeighbors = nextNeighbors
                nextNeighbors = []
        connected.append(newConnectedComponent)
    return connected
edges= [[0,1],[0,2],[3,4],[6,5],[7,8],[8,4]]
n = 10
connectedBFS = bfsConnectedComponents(n,edges)

def dfsConnectedComponents(n,edges):
    neighbors = {}
    visited = set()
    for i in range(n):
        neighbors[i] = []
    for e in edges:
        node1 = e[0]
        node2 = e[1]
        neighbors[node1].append(node2)
        neighbors[node2].append(node1)
    connected = []
 
    def dfs(currentNode):
        if neighbors:
            connected[-1].append(currentNode)
            visited.add(currentNode)
            newN= neighbors.pop(currentNode)
            for neighbor in newN:
                if neighbor not in visited:
                    dfs(neighbor)
    for i in range(n):
        if i not in visited:
            connected.append([])
            dfs(i)
    return connected

edges= [[0,1],[0,2],[3,4],[6,5],[7,8],[8,4]]
n = 10
connectedDFS = dfsConnectedComponents(n,edges)

def dfsHasCycle(n,edges):
    neighbors = {}
    visited = set()
    for i in range(n):
        neighbors[i] = []
    for e in edges:
        node1 = e[0]
        node2 = e[1]
        neighbors[node1].append(node2)
        neighbors[node2].append(node1)   
    def dfs(currentNumber,parentNode):
        if neighbors:
            visited.add(currentNumber)
            newNeighbors = neighbors.pop(currentNumber)
            check = False
            for neighbor in newNeighbors:
                if neighbor == parentNode:
                    continue
                elif neighbor in visited:
                    return True
                else:
                    check = dfs(neighbor,currentNumber)
                    if check:
                        return True
            return check
    return dfs(0,-1)
#edges= [[0,1],[0,2],[1,2],[6,5],[7,8],[8,4]]
#n = 10
#check= dfsHasCycle(n,edges)

def validTree(n,edges):
    neighbors = {}
    visited = set()
    for i in range(n):
        neighbors[i] = []
    for e in edges:
        node1 = e[0]
        node2 = e[1]
        neighbors[node1] = node2
        neighbors[node2] = node1
    def dfs(currentNode,parentNode):
        if neighbors:
            visited.add(currentNode)
            newNeighbors = neighbors.pop(currentNode)
            for n in newNeighbors:
                if n in visited:
                    if n!= parentNode:
                        return True
                else:
                    if dfs(n,currentNode):
                        return True
            return False
    
    return len(visited)==1 and not dfs(0,-1)

edges= [[0,1],[0,2],[1,2],[6,5],[7,8],[8,4]]
n = 10
check= validTree(n,edges)

#Given two strings representing integer numbers ("123" , "30") 
#return a string representing the sum of the two numbers ("153")  
def addInt(string1,string2):
    output = 0
    remain = 0
    num1 = []
    num2 = []
    for s in string1:
        num1.append(s)
    for s in string2:
        num2.append(s)
    c= 0
    while num1 and num2:
        n1 = int(num1.pop())
        n2 = int(num2.pop())
        val = n1+n2+remain
        print (val)
        if val>=10:
            remain=1
            val = val-10
        else:
            remain = 0
        output+=val*10**c
        c+=1
    while num1:
        n1 = int(num1.pop())
        val = n1+remain
        if val>=10:
            remain=1
            val = val-10
        else:
            remain = 0
        output+=val*10**c
        c+=1
    while num2:
        n2 = int(num2.pop())
        val = n2+remain
        if val>=10:
            remain=1
            val = val-10
        else:
            remain = 0
        output+=val*10**c
        c+=1
    if remain:
        output+=remain*10**c
    return output

#Given an array, divide the array into two parts such that the average of these arrays is equal.

    
#A surpasser of an element i in an array is the number of elements greater than 
#i at positions ahead of i in the array. So in this array: [2, 4, 1, 8] the surpassers are [2, 1, 1, 0]. 
#Given an array, find the largest surpasser in the array.

#Given an array, find the highest product possible by multiplying 3 numbers from the array.
#Given two very large numbers represented as strings, return the product.  
def addString(string1,string2):
    output = []
    remain = 0
    num1 = []
    num2 = []
    for s in string1:
        num1.append(s)
    for s in string2:
        num2.append(s)
    while num1 and num2:
        n1 = int(num1.pop())
        n2 = int(num2.pop())
        val = n1+n2+remain
        if val>=10:
            remain=1
            val = val-10
        else:
            remain = 0
        output.append(str(val))
    while num1:
        n1 = int(num1.pop())
        val = n1+remain
        if val>=10:
            remain=1
            val = val-10
        else:
            remain = 0
        output.append(str(val))
    while num2:
        n2 = int(num2.pop())
        val = n2+remain
        if val>=10:
            remain=1
            val = val-10
        else:
            remain = 0
        output.append(str(val))
    if remain:
        output.append(str(remain))
    return "".join(output[::-1])     
def multiply(string1,string2):
    currentString = ""
    for i in range(len(string2)-1,-1,-1):
        number = int(string2[i])
        numberOfZeros= "0"*(len(string2)-1-i)
        output = multiplyOne(string1,number)+numberOfZeros
        currentString= addString(output,currentString)
    return currentString
def multiplyOne(bigNums,oneNum):
    output = []
    remain = 0
    for n in bigNums[::-1]:
        val = int(n)*oneNum+remain
        remain = val//10
        output.append(str(val%10))
    
    return "".join(output[::-1])  

string1 = "12312312390812309182309"
string2 = "123123131232314149999"
output= (multiply(string1,string2))
#Convert sorted array to BST
class BST(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self,val):
        root = self
        
        while root:
            if root.val<val:
                nextNode = root.right
                if not nextNode:
                    root.right = BST(val)
            else:
                nextNode = root.left
                if not nextNode:
                    root.left = BST(val)
            
    def inorder(self):
        root = self
        def toList(root):
            if root:
                output = []
                left = toList(root.left)
                if left:
                    output.extend(left)
                output.append(root.val)
                right = toList(root.right)
                if right:
                    output.extend(right)
                return output
        return toList(root)

def toBST(sortedArray):
    def binarySearch(sortedArray):
        start = 0
        stop = len(sortedArray)-1
        if start <= stop:
            mid = (stop+start)//2
            root = BST(sortedArray[mid])
            left = binarySearch(sortedArray[:mid])
            right = binarySearch(sortedArray[mid+1:])
            root.left = left
            root.right = right
            return root
    return binarySearch(sortedArray)
#One is how to judge a string is palindrome and another is how to judge a tree 
#is a valid binary search tree.          
    
def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True
def isValidBST(root):
    array = [None,None]
    def dfs(root):
        if root:
            left = dfs(root.left)

            if array[0]== None and array[1]== None:
                array[0]=root.val
            elif array[1]== None:
                array[1]= root.val
                if array[0]>= array[1]:
                    return False
            else:
                array[0] = array[1]
                array[1] = root.val
                if array[0]>= array[1]:
                    return False                
            right = dfs(root.right)

            return left and right
        else:
            return True
    return dfs(root)
    
def binaryAddition(a,b):
    output =0 
    remain =0
    c=0
    while a and b:
        first= a%10
        second = b%10
        val = first+second+remain
        if val==1:
            remain =0
        elif val==2:
            remain = 1
            val=0
        elif val==3:
            val=1
            remain=1
        output+=val*10**c
        c+=1
        a = a//10
        b= b//10
    while a:
        first= a%10
        val = first+remain
        if val==1:
            remain =0
        elif val==2:
            remain = 1
            val=0
        elif val==3:
            val=1
            remain=1
        output+=val*10**c 
        c+=1
        a=a//10
    while b:
        first= b%10
        val = first+remain
        if val==1:
            remain =0
        elif val==2:
            remain = 1
            val=0
        elif val==3:
            val=1
            remain=1
        output+=val*10**c 
        c+=1     
        b=b//10
    if remain:
        output+=remain*10**c 
# moving zeros
def moveZeros(array):
    
    return output
