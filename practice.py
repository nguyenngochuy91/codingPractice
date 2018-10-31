#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:14:34 2018

@author: huyn
"""
import random
def binarySearch(sortedArray,n):
    start = 0
    stop  = len(sortedArray)-1
    
    while start <=stop:
        mid   = (stop+start)//2
        midVal = sortedArray[mid]
        if midVal==n:
            return mid
        elif midVal <n:
            start = mid+1
        else:
            stop  = mid-1

    return -1
def isSquare(n):
    if n<=1:
        return n
    start = 0
    stop  = n
    while start <=stop:
        mid   = (stop+start)//2
        if mid**2 == n:
            return True
        elif mid**2 < n:
            start = mid+1
        else:
            stop  = mid-1
    
    return False
    
def getSquare(n):
    if n<=1:
        return n
    start = 0
    stop  = n
    while start <=stop:
        mid   = (stop+start)//2
        if mid**2 == n:
            return True
        elif mid**2 < n:
            start = mid+1
        else:
            stop  = mid-1
    
    return stop

def maximumSubarray(array):
    currentMax = array[0]
    output     = array[0]
    for item in array[1:]:
        currentMax = max(0,currentMax+item)
        output     = max(output,currentMax)
    return output

def findMinSortedArray(arr):
    start = 0
    stop = len(arr)-1
    currentMin = float("inf")
    while start <=stop:
        mid = (start+stop)//2
        currentMin = min(currentMin,arr[mid])
        if arr[mid]<arr[stop]:
            stop = mid -1
        else:
            start = mid+1
    return currentMin

def findMinIndexSortedArray(arr):
    start = 0
    stop = len(arr)-1
    currentMin = float("inf")
    indexMin = None
    while start <=stop:
        mid = (start+stop)//2
        if currentMin > arr[mid]:
            currentMin = arr[mid]
            indexMin  = mid
        if arr[mid]<arr[stop]:
            stop = mid -1
        else:
            start = mid+1
    return indexMin

def searhRotatedSortedArray(arr,n):
    indexMin = findMinIndexSortedArray(arr)
    
    left  = binarySearch(arr[:indexMin],n)
    right = binarySearch(arr[indexMin:],n)
    if left!=-1:
        return left
    if right!=-1:
        return right+indexMin
    return -1

def searhRotatedSortedArray1(arr,n):
    start = 0
    stop = len(arr)-1
    while start <=stop:
        mid = (start+stop)//2
        if arr[mid]==n:
            return mid
        else:
            if arr[mid]<arr[stop]: # right part is sorted
                if n >arr[mid] and n<= arr[stop]:
                    start = mid+1
                else:
                    stop = mid -1
            else:
                # left one is sorted
                if n>=arr[start] and n<arr[mid]:
                    stop -=1
                else:
                    start = mid +1
    return -1

def searhRotatedSortedArrayDuplicated(arr,n):
    start = 0
    stop = len(arr)-1
    while start <=stop:
        mid = (start+stop)//2
        if arr[mid]==n:
            return True
        else:
            if arr[mid]<arr[stop]: # right part is sorted
                if n >arr[mid] and n<= arr[stop]:
                    start = mid+1
                else:
                    stop = mid -1
            elif arr[mid]>arr[stop]:
                # left one is sorted
                if n>=arr[start] and n<arr[mid]:
                    stop -=1
                else:
                    start = mid +1
            else: # if arr[mid] == arr[stop]# decrement the size
                stop-=1
    return False

"""
Given an m x n matrix of non-negative integers representing the height of each 
unit cell in a continent, the "Pacific ocean" touches the left and top edges of 
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell 
to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
def pacificAtlanticWaterFlow417(matrix):
    m = len(matrix)
    if m==0:
        return []
    n = len(matrix[0])
    moves = [(0,1),(0,-1),(-1,0),(1,0)]
    
    def dfs_call(i,j,visited):
        visited[i][j] = True
        for mi, mj in moves:
            ni, nj = i+mi, j+mj
            if ni>=0 and ni<m and nj>=0 and nj<n and not visited[ni][nj] and matrix[ni][nj]>=matrix[i][j]:
                dfs_call(ni,nj,visited)
    
    visited_atl = [[False for _ in range(n)] for _ in range(m)]
    for j in range(n):
        dfs_call(m-1,j,visited_atl)
    for i in range(m):
        dfs_call(i,n-1,visited_atl)
        
    visited_pac = [[False for _ in range(n)] for _ in range(m)]
    for j in range(n):
        dfs_call(0,j,visited_pac)
    for i in range(m):
        dfs_call(i,0,visited_pac)
    
    result = []
    for i in range(m):
        for j in range(n):
            if visited_atl[i][j] and visited_pac[i][j]:
                result.append([i,j])
    
    return result

#Implement Trie 208
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current =self.root
        for char in word:
            if char not in current:
                current[char]= {}
            current = current[char]
        current["#"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current =self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return "#" in current     

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current =self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

#Implement WordDictionary 211
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}      

    def addWord(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current =self.root
        for char in word:
            if char not in current:
                current[char]= {}
            current = current[char]
        current["#"] = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the 
        dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        def dfs(word,index,root):
            currentChar = word[index]
            if index==len(word)-1:
                if currentChar in root and "#" in root[currentChar]: # the char is in
#                    print (285)
                    return True
                elif currentChar =="." and len(root)>=1:
                    
                    for item in root:
                        if item !="#":
                            if "#" in root[item]:
                                print (292)
                                return True
#                    print (293())
                    return False
                else:
#                    print (297)
                    return False          
            else:
#                print (currentChar)
                if currentChar in root: # the char is in
#                    print(302)
                    return dfs(word,index+1,root[currentChar])
                elif currentChar =="." and len(root)>=1:
                    check =False
                    for char in root:
                        if char!="#":
                            check = dfs(word,index+1,root[char])
                        if check:
                            print(310)
                            return True
#                    print (312)
                    return False
                else:
#                    print(315)
#                    print (root)
                    return False    
        return dfs(word,0,root)


# Insert delete get random 380

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary= {}
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dictionary:
            self.dictionary[val]=True
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dictionary:
            return False
        self.dictionary.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.dictionary.keys())


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def wordSearch79(board,word):
    r = len(board)
    if not r:
        return False
    c = len(board[0])
    moves = [(0,1),(0,-1),(-1,0),(1,0)]  
    def dfs(word,index,i,j,visited):
        w = word[index]
        if index == len(word)-1:
            if board[i][j] == w:
                return True
            else:
                
                return False
        else:
            if board[i][j] == w:
                visited[i][j]=True
                check = False
                for m in moves:
                    x = i+m[0]
                    y = j+m[1]
                    if x>=0 and x<r and y>=0 and y<c:
                        if not visited[x][y]:
                            check = dfs(word,index+1,x,y,visited)
                    if check:
                        return True
              
                visited[i][j]=False
                return check
            else:
                
                return False
    for i in range(r):
        for j in range(c):
            visited = [[False for i in range(c)] for j in range(r)]
            if dfs(word,0,i,j,visited):
                return True
    return False
        
def flatten(iterable):
    result = []
    for nestedL in iterable:
        if type(nestedL) ==list:
            result.extend(flatten(nestedL))
        else:
            result.append(nestedL)
    return result
    
def courseScedule207(numCourses,prerequisites):
    d= {} # key is the course to take, value is the prerequisite
    for p in prerequisites:
        course = p[0]
        preR   = p[1]
        if preR in d:
            if course in d[preR]:
                return False
        else:

            for k in d:
                if course in d[k]:
                    d[k][preR]=1
            if course not in d:
                d[course]={}                
            d[course][preR]=1
#        print (d)
    return True
#lru146
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = []
        self.capacity = capacity
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = -1
        for i in range(len(self.cache)):
            item = self.cache[i]
            if item[0] == key:
                val= item[1]
                self.cache.pop(i)
                self.cache.append([key,val])
                break
            
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        for i in range(len(self.cache)):
            item = self.cache[i]
            if item[0]==key:
                self.cache.pop(i)
                self.cache.append([key,value])
                return                
        if len(self.cache) == self.capacity:
            self.cache.pop(0)
            self.cache.append([key,value])
        else:
            self.cache.append([key,value])
                
                
