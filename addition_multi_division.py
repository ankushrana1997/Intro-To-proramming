def addition(a,b):
    x=a
    y=b
    printf("Addition of two number"+a+b)

def multiply(a,b):
    x=a
    y=b
    printf("Addition of two number"+x*y)
 
 def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['t','u','t','o','r','i','a','l']
x = 'a'
print("element found at index "+str(linearsearch(arr,x)))
