def perimeter_rectangle(length,breadth):
    p=2*(length+breadth)
    return p
   
def area_rectangle(length,breadth=2):
    a=length*breadth
    return a
    
l=int(input('Enter the Length :'))
b=int(input('Enter the breadth :'))

print(perimeter_rectangle(l,b))
print(area_rectangle(l,b))


