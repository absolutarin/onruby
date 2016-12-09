#import list

arr = []
arr = (raw_input("Enter anything: "))
print "Array is: %s" %arr
print "Length of array is: %d" %len(arr)

i = 0
while ( i<len(arr)):
    newarr = (arr[i]+arr[i+1]+arr[i+2])
    print newarr
    i = i+3

