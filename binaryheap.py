class maxPQ(object):
    """docstring for ClassName"""
    def __init__(self, pq,N):
        super(maxPQ, self).__init__()
        self.pq = pq
        self.N = N
    
    def parent(self,k):
        return int(k/2)

    def left(self,k):
        return 2*k

    def right(self,k):
        return 2*k+1

    def less(self,k,j):
        if self.pq[k] < self.pq[j]:
            return True
        else:
            return False

    def exch(self,k,j):
        temp = self.pq[k]
        self.pq[k] = self.pq[j]
        self.pq[j] = temp

    def maxPQvalue(self):
        return self.pq[1]

    def swim(self,k):
        while k>1 and self.less(self.parent(k),k):
            self.exch(self.parent(k),k)
            k = self.parent(k)

    def sink(self,k):
        while self.left(k)<self.N:
            older = self.left(k)
            if self.right(k)<self.N and self.less(older,self.right(k)):
                older = self.right(k)
            if self.less(older,k):
                break
            self.exch(k,older)
            k = older


    def insertPQ(self,e):
        self.N = self.N+1
        self.pq.append(e)
        self.swim(self.N)


    def delMax(self):
        max_value = self.pq[1]
        self.exch(1,self.N)
        self.pq.pop()
        self.N = self.N - 1
        self.sink(1)
        return max_value


if __name__ == '__main__':
    student = maxPQ([0,1],1)
    student.insertPQ(2)
    for i in range(2,10):
        student.insertPQ(i) 
    print(student.maxPQvalue())
    print(student.delMax())
    print(student.maxPQvalue())