###################pigeonhole search##################
def pigeonholeSearch(arr):
    holes = [[] for i in range(max(arr)-min(arr)+1)]
    for i in arr:
        holes[i-min(arr)].append(i)
    return [i for i in holes]
#print(pigeonholeSearch([3,7,4,15,2,3,5]))



