n = int(input())

wordList = []
for i in range(n):
  wordList.append(input())

wordList.sort(key=lambda x: len(x))

prefixX = []
for i in range(n):
  for j in range(i+1, n):
    if wordList[i] in wordList[j][:len(wordList[i])]:
      break
  else:
    prefixX.append(wordList[i])

print(len(prefixX))