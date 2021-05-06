#List are mutable
number = [2,34,100,1,9]
#operations on list
number.append(2)
print(number)
number.remove(100)
print(number)
number.pop()
print(number)
print(len(number))
print(max(number))
print(min(number))
number.sort()
print(number)
print(type(number))
number.extend([4,5])
print(number)
#Tuple is immutable
tp = (1,2,6)
print(tp)
print(type(tp))