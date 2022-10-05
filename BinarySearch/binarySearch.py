def BinarySearch(lt,key):
    l = 0
    h = len(lt)
    for i in range(len(lt)):
        mid = (l+h)//2
        if key == lt[mid]:
            return mid+1
        elif key < lt[mid]:
            h = (mid+l)//2
        elif key>lt[mid]:
            l = (mid+h)//2
    return -1

lt = [17, 45, 15, 84, 28, 51, 13, 29, 47, 63]
print(BinarySearch(lt,key = 51))
