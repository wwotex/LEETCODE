L = [1,5,4,3,2]

def mergeSort(ls):
    mid = (len(ls)//2)
    if mid == 0:
        return ls
    ls1 = mergeSort(ls[:mid])
    ls2 = mergeSort(ls[mid:])
    return merge(ls1, ls2)

def merge(ls1, ls2):
    result = []
    while ls1 and ls2:
        if ls1[0] < ls2[0]:
            result.append(ls1.pop(0))
        else:
            result.append(ls2.pop(0))
    
    while ls1:
        result.append(ls1.pop(0))
    
    while ls2:
        result.append(ls2.pop(0))
    return result

print(mergeSort(L))