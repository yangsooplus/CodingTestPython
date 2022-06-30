word = input()
new_word = ''

minidx = 0
first = word[0]
for i in range(0, len(word)-2):
  if first > word[i]:
    minidx = i
    first = word[i]
  elif first == word[i]:
    if i > 0 and word[i-1] < word[minidx-1]:
      minidx = i
      first = word[i]

for i in range(minidx, -1, -1):
  new_word += word[i]

minidx2 = minidx+1
second = word[minidx+1]
for i in range(minidx2, len(word)-1):
  if second > word[i]:
    minidx2 = i
    second = word[i]
  elif second == word[i]:
    if i > 0 and word[i-1] < word[minidx2-1]:
      minidx2 = i
      second = word[i]

for i in range(minidx2, minidx, -1):
  new_word += word[i]

for i in range(len(word)-1, minidx2, -1):
  new_word += word[i]

print(new_word)