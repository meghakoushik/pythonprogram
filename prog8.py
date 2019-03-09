# program to create a histogram from a given list of integer.


def histogram(number):                  #define function
     for n in number:
        result = ''
        temp = n
        while(temp > 0):
          result += '*'
          temp = temp-1
        print(result)                    #print output

histogram([4,3,9,5])                     #function call







