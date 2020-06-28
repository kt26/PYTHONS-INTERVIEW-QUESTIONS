import math

def merge(array1,array2):
    result_array = []
    
    while(len(array1)>0 and len(array2)>0):
        if array1[0]<array2[0]:
            result_array.append(array1[0])
            array1 = array1[1:]
        else:
            result_array.append(array2[0])
            array2 = array2[1:]

    return result_array + array1 + array2



def mergesort(array):
    if len(array)==1:
        return array

    mid = math.floor(len(array)/2)

    return merge(mergesort(array[:mid]),mergesort(array[mid:]))



my_array = [2,1,33,4,5,61,2,13,45,5,6,9,4,2,2,12,11]

print (mergesort(my_array))
