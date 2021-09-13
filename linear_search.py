# def linear_search(list, target):
#     """return the index position of the target if found , else return none"""

#     for i in range(0 ,len(list)):
#         if list[i]==target:
#             return i
#         return None

# def verify(index):
#     if index is not None:
#         print("target found at index:",index)
#     else:
#         print("target not found in list")

# numbers=[1,2,3,4,5,6,7,8,9,10]

# result=linear_search(numbers, 6)
# verify(result)


# def power(base, exp):
#     if exp ==0:
#         return 1
#     if exp ==1:
#         return base
#     return base * power(base, exp-1)
    
# print(power(2,2)) 


# def decimalToBinary(n):
#     if n ==0:
#         return 1
#     else:
#         return n%2 + 10 * decimalToBinary(int(n/2))

# print(decimalToBinary(10))


# import array as np

# twoDarray= np.array([[11,15,10,6],[10,14,16,8],[3,6,9,5],[12,19,17,1]])
# print(twoDarray)

# def traverseTDrray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])
# traverseTDrray(twoDarray)

# newTDarray = np.delete(twoDarray, 0, axi= 0)
# print(newTDarray)


from array import *

# ///create an array and traverse///

my_array = array('i', [1,2,3,4,5,])
for i in my_array:

    print(i)

#access individual element through indexes
print("step 2")
print(my_array[0])


# append any valur to the array using append()


print( 'step 3')
my_array.append(6)
print(my_array)


# nsert value in an array using insert()

print('step 4')
my_array.insert(0, 11)
print(my_array)

# extend python array 

print("step 5")
my_array1=array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)

# add item from list into array

print('stp6')

tempList=[20,21,22]
my_array.fromlist(tempList)
print(my_array)

# remove item
print('stp7')

my_array.remove(22)
print(my_array)







































