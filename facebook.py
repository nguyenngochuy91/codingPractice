#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:42:34 2018

@author: huyn
"""
try:
    from queue import Queue as q
except:
    from Queue import Queue as q
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

def findNextNot0(array,index):
    for i in range(index,len(array)):

        if array[i]!=0:
            return i
    return -1
def findNext0(array,index):
    for i in range(index,len(array)):
        if array[i]==0:
            return i
    return -1    

def moveZeroes(array):

    first = 0
    second = 0
    while second <len(array) and first <len(array):
        first = findNext0(array,first)
        if not first-1:
            break
        second  = findNextNot0(array,first)
        if second==-1:
            break # not finding any more not 0
        else: # swap those 2 index
            array[first]=array[second]
            array[second]=0
            first+=1


# traverse a tree vertically
def traverseVertically(root):
    output = []
    d = {}
    newq = q()
    newq.put([root,0])
    currentMin = float("inf")
    currentMax = -float("inf")
    while not newq.empty():
        info = newq.get()
        currentNode = info[0]
        level = info[1]
        currentMin= min(currentMin,level)
        currentMax= max(currentMax,level)
        if level not in d:
            d[level] = [currentNode.val]
        else:
            d[level].append(currentNode.val)
        left = currentNode.left
        if left:
            newq.put([left,level-1])
        right = currentNode.right
        if right:
            newq.put([right,level+1])
    for i in range(currentMin,currentMax+1):
        try:
            output.extend(d[i])
        except:
            continue

    return output
#Write a function to return if two words are exactly "one edit" away, where an edit is:
#
#Inserting one character anywhere in the word (including at the beginning and end)
#Removing one character
#Replacing exactly one character
def isOneEditAway(string1,string2):
    if abs(len(string1)-len(string2))>=2:
        return False
    else:
        c = 0
        i = 0
        j = 0
        while i <len(string1) and j <len(string2):
            if string1[i]!= string2[j]:
                if c ==1:
                    return False
                else:
                    c+=1
                    if len(string1)>len(string2):
                        i+=1
                    elif len(string1)<len(string2):
                        j+=1
                    
            else:
                i+=1
                j+=1
                
    return True

def editDistance(string1,string2):
    matrix = []
    return matrix[-1][-1]
#Given array with integer find local minimum. log(n)

#Given number 743 find the number from the same digits that is smaller than the given and biggest possible.
#Regex matching 
    
#Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

#Return the quotient after dividing dividend by divisor.
#
#The integer division should truncate toward zero.
#
#Example 1:
#
#Input: dividend = 10, divisor = 3
#Output: 3
#Example 2:
#
#Input: dividend = 7, divisor = -3
#Output: -2
    
#nput [5,6,10] Output [60,50, 30]
#At every index the product should be product of all except the index.  

#Continous subsequence with target 
    
#Return the smallest two numbers in an array.  
    
#Q: Sort a binary tree  
    
#determine all the rotatable numbers of length k  
    
#about dynamic programming and quick select  
    
#Solve a set of equations [["A","B","C"], ["C","1"], ["B","C","1"], ["D","B","1"]] 
#representing A = B + C, etc. The first element is always followed by an equal sign, 
#and there is only + operator. The solution need to returned as a dictionary.  
    
#Given a massive grid of ones an zeroes, and given a subgrid of this, calculate 
#the number of ones in the subgrid.  
    
#Given a singly-linked list, print the values in reverse order 
    
#Write the partition method for Quicksort  
    
#Given an array of integers, determine if a subarray exists whose sum is a target value 
    
#Tax bracket array question  
    
#Given an unsorted integer array with a target sum, return all possible triplets 
#of numbers within the array that add up to the target sum.  
    
#Flatten binary tree to doubly linked list
    
#coding questions. clone graph  
    
#Implement readLine given read4k  
    
#Given an integer array, find if the target sum exists as the sum of contiguous elements.  
    
#    Given 2 arrays of numbers, return true if 3 consecutive numbers in array A, 
#add up to a number in array B. Return false otherwise.  
    
#Given a hash map information, show all the permutation that could be the possible answer  
    
# heap problem
    
#There is a 2d grid composed of 0 and 1. 0 means empty grid and 1 means obstacle.
#Q1: Can you reach the bottom right corner starting from the upper left corner?
#Q2: Print all possible paths.
#Q3: Find the shortest path.  
    

#1. 2-SUM in sorted array
    
#1. Remove invalid parentheses
#2. Leetcode: Walls and Gates
#3. Leetcode: Flatten Nested List Iterator
    
#iven an array of Nodes. Decide whether they can form a binary tree  
    
#Is a string Palindrome ? If not, Can the string be made a palindrome after removing a character from that String?  
    
#Given a boolean array Cal = [F,F,F,T,T,F,T,T] where T: On vacation F: Not on vacation.
#Given an integer variable PTO (1)
#Find the set of days with maximum vacation if PTO were utilised.  
    
#Convert integer to English. (e.g. 100 -> one hundred; 12345->twelve thousand three hundred forty five  
    
#Sort an unsorted linked list from smallest to biggest  
    
#Checking if Linked List is palindromic  
    
#The optimal way of sorting while traversing an array
    
#Given an array of numbers(ex [3 2 5]), find if its possible to split it into 2 
#parts with equal sum without reordering (ex [3 2 ] and [5] ) and false if not possible!  
    
#Write a program to record the largest ascending sequence, given an array of integers. 