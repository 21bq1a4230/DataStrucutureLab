class queue:
    def __init__(self):
        self.lt = []
        self.l = 0
    def push(self,item):
        self.lt.insert(0,item)
        self.l += 1
    def pop(self):
        print(self.lt.pop(self.l-1))
        self.l -= 1
        if len(self.lt) == 0:
            print("queue is underflowing")

size = int(input("enter the size of the queue"))
q = queue()
print("enter",size,"no of elements")
for i in range(size):
    q.push(int(input()))
    
opt = input("type pop for popping and exit to exit")
if opt.casefold() == 'pop':
    for i in range(size):
        q.pop()
if opt.casefold() == 'exit':
     exit()
     