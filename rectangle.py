def perimeter_Rectangle(length,breadth):
    p=2*(length+breadth)
    return p
   
def area_Rectangle(length,breadth):
    a=length*breadth
    return a
    
l=int(input('Enter the Length :'))
b=int(input('Enter the breadth :'))

print(perimeter_rectangle(l,b))
print(area_rectangle(l,b))


