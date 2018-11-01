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
def findLocal(array):
    if len(array)==1:
        return array[0]
    if array[0]<=array[1]:
        return array[0]
    for i in range(1,len(array)-1):
        if array[i]<=array[i]-1 and array[i]<=array[i]+1:
            return array[i]

    return array[-1]       
def findLocalBST(array):
    start = 0
    stop  = len(array)-1
    while start<=stop:
            mid = (start+stop)//2
            if array[mid]<=array[mid+1] and array[mid]<=array[mid-1]:
                return array[mid]
            elif array[mid]>array[mid-1]:
                stop = mid-1
            else:
                start = mid+1
                
def flattenList(array):
    output = []
    for item in array:
        if type(item)==list:
#            print (item)
            subarray= flattenList(item)
            output.extend(subarray)
        else:
            output.append(item)
    return output
    
#Given number 743 find the number from the same digits that is smaller than the given and biggest possible.
def findBiggest(string):
    string = list(string)
    if sorted(string)== string:
        return "".join(string)
    elif sorted(string,reverse= True) == string:
        # swap the last two not equal
        for i in range(len(string),0,-1):
            if string[i]!=string[i-1]:
                temp = string[i]
                string[i] = string[i-1]
                string[i-1]=temp
                return "".join(string)
        return "".join(string)
    else:
        return ""
             
    
#Given an array of integers, determine if a subarray exists whose sum is a target value 
def subArraySum(arr, n, sum): 
      
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    curr_sum = arr[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print ("Sum found between indexes") 
            print ("%d and %d"%(start, i-1)) 
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
  
    # If we reach here,  
    # then no subarray 
    print ("No subarray found") 
    return 0


class Link(object):
    def __init__(self,val,next= None):
        self.val = val
        self.next= next
    def reverse(self):
        prev= None
        current = self
        while current:
            head= current
            next= current.next
            current.next = prev
            prev= current
            current = next
        print (head.val)
        return head
#1. 2-SUM in sorted array

#Write the partition method for Quicksort  
      
#Find all triplets with zero sum
def findTruplets(arr,n):
    found = False
    arr.sort()
    for i in range(0,n-1):
        # initialize left and right
        l = i+1
        r = n-1
        x = arr[i]
        while l<r:
            current = x+arr[l]+arr[r]
            if (current==0):
                print (x,arr[l],arr[r])
                l+=1
                r-=1
                found = True
            elif (current<0):
                l+=1
            else:
                r-=1
    if found == "False":
        print ("None")
    
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
