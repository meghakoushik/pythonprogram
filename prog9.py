#program to concatenate all elements in a list into string and return it.


#with Function

def concatenate_list(list):                            #create a function
    result = ''
    for element in list:
            result += str(element)                     #convert integer to string and store result
    return


print(concatenate_list([1, 5, 12, 2]))                 #function calling



#without function

list = [1,3,4,5,6]
result= ''
for i in list:

   result += str(i)                                    #convert integer to string and store result


print(result)                                          #output result