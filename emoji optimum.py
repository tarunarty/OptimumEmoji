"""
start with x

two operations - [C] copy paste (expense - 5, doubles cur)
               - [P] paste (expense - 2, cur remains constant)

reach N with minimum expense.

we need the path and the expense.

print all the paths and fine the one with the minimum expense.

"""

#functions
"""
paste {function}- Increases present value by the clipboard value
                  cost += 2
copy_paste {function}- changes clipboard value to present value,
                       doubles present value
                       cost += 5
"""


def paste(cost, l, clip):
    lis = l.copy()
    if lis[-1]>100:
        return [[cost],lis,[clip]]
    lis.append(lis[-1]+clip)        
    k = [[cost+2], lis , [clip]]
    return k

def copy_paste(cost, l, clip):
    lis = l.copy()
    if lis[-1]>100:
        return [[cost],lis,[clip]]
    lis.append(lis[-1]+lis[-1])
    k = [[cost+5], lis, [lis[-2]]]
    return k

def write(cost, l, clip):
    lis = l.copy()
    if lis[-1]>100:
        return [[cost],lis,[clip]]
    lis.append(lis[-1]+1)
    k = [[cost+1], lis, [clip]]
    return k

    

n = 12
lis = [[[1],[1],[0]]]
while n:

    k = len(lis)
    for i in range(k):
        
        temp = lis[i]
        
        t_cost = temp[0][0]
        t_lis = temp[1]
        t_clip = temp[2][0]

        p = paste(t_cost, t_lis, t_clip)
        c = copy_paste(t_cost, t_lis, t_clip)
        w = write(t_cost, t_lis, t_clip)
        
        lis.append(p)
        lis.append(c)
        lis.append(w)
    lis = lis[k:]
    #print(lis)
    n-=1
    
lis.sort()
for i in range(len(lis)):
    elem = lis[i]
    if elem in lis[i+1:]:
        pass
    #elif elem[1][-1]<100:
        #pass
    else:
        print("cost: ", elem[0])
        print("path: ", elem[1])
        print()
        #break
    
"""
optimal to 100
[[25], [1, 2, 3, 4, 5, 6, 12, 18, 36, 54, 108], [54]]
[[25], [1, 2, 3, 4, 5, 6, 12, 18, 36, 72, 108], [36]]
[[25], [1, 2, 3, 4, 5, 6, 12, 24, 36, 72, 108], [36]]
[[25], [1, 2, 3, 4, 5, 10, 11, 22, 33, 66, 99], [33]]
[[25], [1, 2, 3, 4, 8, 12, 24, 36, 72, 108], [36]]
[[25], [1, 2, 3, 4, 8, 12, 24, 36, 72, 108], [36]]

{highest in 25 moves was 112 for 1,2,3...7}
"""
















