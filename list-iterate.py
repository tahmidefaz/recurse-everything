def iterate(li,count):
  if(count == len(li)-1):
    pass
  else:
    count += 1
    print(li[count])
    iterate(li,count)

l1 = [1,2,3,4,5,6,7]
l2 = [7,6,5,4,3,2,1]

iterate(l1,0)
