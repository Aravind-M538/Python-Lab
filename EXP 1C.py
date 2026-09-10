from itertools import combinations
list = [-1,2,-3,4,-5,6,-7]
print("positive combinations")
for r in range(1,len(list)+1):
    for combo in combinnations(list,r):
        if all(num>0 for num in combo):
            print(combo)
