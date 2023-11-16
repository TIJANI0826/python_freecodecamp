import numpy as np

def calculate(list):
  #if isinstance(list,list) == False:
  #  return "This is not a standard python list"
  if len(list) < 9:
      raise ValueError("List must contain nine numbers.")
  a = np.array(list)
  b = np.array(list).reshape(3,3)
  calculations = {
    'mean' : [[a for a in b.mean(axis=0)],[a for a in b.mean(axis=1)],b.mean()],
    'variance' : [[a for a in np.var(b, axis=0)],[a for a in np.var(b, axis=1)],np.var(a)],
    'standard deviation' : [[a for a in b.std(axis=0)],[a for a in b.std(axis=1)],a.std()],
    'max' : [[a for a in b.max(axis=0)],[a for a in b.max(axis=1)],a.max()],
    'min' : [[a for a in b.min(axis=0)],[a for a in b.min(axis=1)],a.min()],
    'sum' : [[a for a in b.sum(axis=0)],[a for a in b.sum(axis=1)],a.sum()]
  }

  return calculations

a = calculate([2,6,2,8,4,0,1,5,7])
print(a)