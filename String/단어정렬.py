n = int(input())

wordList = []
for i in range(n):
  wordList.append(input())

wordList = list(set(wordList))

# 사전 순으로 미리 정렬
wordList.sort()

# 사전 순 리스트를 길이별로 정렬
# 같은 길이 내에서 사전 순으로 정렬
wordList.sort(key=lambda x : len(x))

for w in wordList:
  print(w)