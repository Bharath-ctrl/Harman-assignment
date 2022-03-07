#wa python program to square and cube every number in a given list of integers using lambda
list1=[2,3,4,45,67,78]
square=list(map(lambda x: x**2,list1))
cube=list(map(lambda x: x**3,list1))
print(f'Squares are:{square}\nAnd the cubes are: {cube}')