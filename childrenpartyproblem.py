def points_covered(x):
    R = []
    i = 0
    while(i<len(x)):
        [l,r] = [x[i], x[i]+1]
        R.append([l,r])
        i = i+1
        while(i<len(x) and x[i]<=r):
            i = i+1
    return len(R)
x = [5.5,5.5,5.8,6,7.8,8.2]
print(points_covered(x))
