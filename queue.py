class queue:
    def __init__(self):
        self.que = []
    def enq(self, x):
        self.que.append(x)
    def deq(self):
        self.que.pop(0)

    def show(self):
        if len(self.que) == 0:
            print("List is Empty")
        else:
            print(self.que, ' ')



q = queue()
print("Enqueue 10")
q.enq(10)
q.show()
print("Enqueue 20")
q.enq(20)
q.show()
print("Enqueue 30")
q.enq(30)
q.show()
print("Enqueue 40")
q.enq(40)
q.show()
print("Dequeue")
q.deq()
q.show()
print("Dequeue")
q.deq()
q.show()
print("Dequeue")
q.deq()
q.show()
print("Dequeue")
q.deq()
q.show()