def Era(n, k):
  nums = [i for i in range(2, n+1)]
  delete = 0

  while delete < k:
    base = nums.pop(0)
    delete += 1
    
    if delete == k:
        print(base)
        return
    
    for n in nums:
      if n%base == 0:
        dn = n
        nums.remove(n)
        delete += 1
        if delete == k:
          print(dn)
          return
    

n, k = map(int, input().split(' '))
Era(n, k)