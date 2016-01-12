class PriorityQueue:
    """Heap-based priority queue implementation."""
    def __init__(self):
        """initially empty priority queue."""
        self.queue=[None]
    

    def append(self,key):
        if key is None:
            raise ValueError('Cannot insert None in the queue')

        i=self.size()
        self.queue.append(key)
        while i>1:
            parent=i/2
            if key>=self.queue[parent]:
                break
            self.queue[i]=self.queue[parent]
            self.queue[parent]=key
            i=parent
    
    def min(self):
        if self.size<=1:
            return None
        return self.queue[1]
    
    def pop(self):
        if self.size()<=1:
            return None
        heap=self.queue
        popped_key=heap[1]
        if self.size()==2:
            return heap.pop()
        heap[1]=heap.pop()
        i=1
        while True:
            left=2*i
            right=2*i+1
            if left>=self.size():
                break
            if heap[i]<heap[left]:
                min=i
            else:
                min=left
            if right>=self.size():
                break
            if heap[right]<heap[min]:
                min=right
            if i==min:
                break
            else:
                tem=heap[i]
                heap[i]=heap[min]
                heap[min]=tem
                i=min
        return popped_key
                  
                                  
    def size(self):
        # num of elements +1
        return len(self.queue)