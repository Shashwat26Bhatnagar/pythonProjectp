from queue import PriorityQueue
q=PriorityQueue()
q.put((10,'Red balls'))
q.put((8,'Pink ball'))
q.put((5,'White ball'))
q.put((4,"Green ball"))
while not q.empty():
    item=q.get()
    print(item)