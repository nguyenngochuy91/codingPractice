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
    
    return len(visited)==n and not dfs(0,-1)

edges= [[0,1],[0,2],[1,2],[6,5],[7,8],[8,4]]
n = 10
check= validTree(n,edges)

