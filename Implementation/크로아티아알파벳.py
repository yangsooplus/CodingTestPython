Kroatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

st = input()
cnt = 0
for k in Kroatia:
  if k in st:
    cnt += st.count(k)
    st = st.replace(k, '-')

print(cnt+len(st)-st.count('-'))