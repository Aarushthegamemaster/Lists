L = [4, 5, 1, 2, 7, 9, 10, 8]
print("Original List:" , L)

count = 0

for i in L:
    count += 1

avg = sum(L)/len(L)
print("The average of the list is", avg)
print("The sum of the list is", sum(L))

L.sort()

print("The smallest element in the list is", L[0])
print("The largest element in the list is", L[-1])
