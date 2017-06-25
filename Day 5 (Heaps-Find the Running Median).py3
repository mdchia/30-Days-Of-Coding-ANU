#!/bin/python3

import sys

class Heap():
    def __init__(self, heap_type="min"):
        self.heap=[0]
        self.size=0
        self.root=self.heap[0]
        if heap_type=="min" or heap_type=="max":
            self.heap_type=heap_type
        else:
            raise AttributeError("Must be a min or max heap!")
    def heapifyAdd(self,i):
        while i // 2 > 0:
            if self.heap_type=="min":
                switchy=(self.heap[i] < self.heap[i // 2])
            else:
                switchy=(self.heap[i] > self.heap[i // 2])
            if switchy:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2
    def add(self, a):
        self.heap.append(a)
        self.size+=1
        self.heapifyAdd(self.size)
        self.root=self.heap[1]
    def heapifyRemove(self,i):
        while (i * 2) <= self.size:
            mc = self.mChild(i)
            if self.heap_type=="min":
                switchy=(self.heap[i] > self.heap[mc])
            else:
                switchy=(self.heap[i] < self.heap[mc])
            if switchy:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc
    def mChild(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_type=="min":
                switchy=(self.heap[i*2] < self.heap[i*2+1])
            else:
                switchy=(self.heap[i*2] > self.heap[i*2+1])
            if switchy:
                return i * 2
            else:
                return i * 2 + 1
    def poll(self):
        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.heapifyRemove(1)
        return root

def balance(minHeap,maxHeap):
    if(minHeap.root<maxHeap.root and minHeap.size!=0 and maxHeap.size!=0):
        tmpBig=minHeap.poll()
        tmpSmall=maxHeap.poll()
        minHeap.add(tmpSmall)
        maxHeap.add(tmpBig)

n = int(input().strip())
a_i = 0
minHeap=Heap("min")
maxHeap=Heap("max")
for a_i in range(n):
    a_t = int(input().strip())
    if minHeap.size <= maxHeap.size:
        minHeap.add(a_t)
    else:
        maxHeap.add(a_t)
    balance(minHeap,maxHeap)
    if maxHeap.size==minHeap.size:
        print(float((minHeap.root+maxHeap.root)/2))
    else:
        print(float(minHeap.root))
    #print(minHeap.heap)
    #print(maxHeap.heap)
