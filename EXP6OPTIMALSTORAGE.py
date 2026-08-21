n = int(input("Enter number of files: "))

length = []

print("Enter the length of each file:")
for i in range(n):
    x = int(input(f"File {i + 1}: "))
    length.append(x)

for i in range(n - 1):
    for j in range(i + 1, n):
        if length[i] > length[j]:
            temp = length[i]
            length[i] = length[j]
            length[j] = temp



total = 0
RT = 0

for i in range(n):
    RT = RT + length[i]
    total = total + RT

MRT = total / n

print("\nOptimal Order:", length)
print("Total Retrieval Time:", total)
print("Mean Retrieval Time (MRT):", MRT)