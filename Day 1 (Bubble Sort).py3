n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps=0
round_swaps=1
while round_swaps>0:
    round_swaps=0
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            round_swaps+=1
            swaps+=1

print("Array is sorted in "+str(swaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[-1]))
