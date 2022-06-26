def makeFelindrom(oddabc, abclist):
  result = oddabc
  while abclist:
    pop = abclist.pop()
    result = pop + result + pop
  print(result)

def oddCheck(abc, oddabc):
  abclist = []
  abcitems = sorted(abc.items())

  for item in abcitems:
    if item[1]%2 == 1:
      if oddabc == '':
        oddabc = item[0]
        abc[oddabc] -= 1
        if abc[oddabc] > 0:
          abclist += [oddabc*(abc[oddabc]//2)]
      else:
        print('I\'m Sorry Hansoo')
        return
    else:
      abclist += [item[0]*(item[1]//2)]
  makeFelindrom(oddabc, abclist)
  
st = input()
abc = {}

for s in st:
  if s in abc.keys():
    abc[s] += 1
  else:
    abc[s] = 1

oddabc = ''
oddCheck(abc, oddabc)