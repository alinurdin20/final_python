def buble(arr):
    n = len(arr)
    for i in range(n):
        for j  in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

data = [64,89,34,23,78,90]
buble(data)
print(data)
print("==================")

def y(x):
    n = len(x)
    for i in range(n):
        for j in range(0,n-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1]= x[j+1], x[j]
                                        
dataH = ["B","T","J","K"]
y(dataH)
print(y)