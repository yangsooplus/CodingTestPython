word = input()
wordList = []


for i in range(1, len(word)-1):
  for j in range(i+1, len(word)):
    first = list(word[0:i])
    second = list(word[i:j])
    third = list(word[j:])

    first.reverse()
    second.reverse()
    third.reverse()
    w = ''.join(first + second + third)
    wordList.append(w)

wordList.sort()
print(wordList[0])
    