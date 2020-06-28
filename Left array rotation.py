d = int(input("Enter number of left rotation : "))

a = list(map(int, input("Enter array space seprated : ").rstrip().split()))

print(*(a[d%len(a):]+a[:d%len(a)]))