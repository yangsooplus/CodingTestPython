w, h, b = map(int, input().split())
require = (w*h*b)/(8*1024*1024)
print("%.2f MB" %require)