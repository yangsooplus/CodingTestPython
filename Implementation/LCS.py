# Longest Common Subsequence
# 최장 공통 부분수열 구하는 문제다. 
# 알고리즘은 블로그를 참고했다.

st1 = "-" + input()
st2 = "-" + input()

arr = [[0 for j in range(len(st2))] for i in range(len(st1))]

for i in range(len(st1)):
  for j in range(len(st2)):
    if i == 0 or j == 0: # 마진 값 설정
      arr[i][j] = 0
    elif st1[i] == st2[j]:
      arr[i][j] = arr[i-1][j-1] + 1
    else:
      arr[i][j] = max(arr[i-1][j], arr[i][j-1])


print(arr[i][j])
'''
# LCS 구하는 과정 
i = len(st1) - 1
j = len(st2) - 1
result = ''
while True:
  cur = arr[i][j]
  if cur == 0:
    break
  if arr[i-1][j] == cur:
    i -= 1
  elif arr[i][j-1] == cur:
    j -= 1
  else:
    result = st1[i] + result
    i -= 1
    j -= 1
    
print(len(result))
'''