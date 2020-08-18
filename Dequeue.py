class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())