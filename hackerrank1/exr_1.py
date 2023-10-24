import array

def simpleArraySum():
  print ("Hello, how many elements do you want to have in the array: ")
  array_len = input()
  my_arr = array.array('i', int(array_len) * [1])
  for x in range(0, int(array_len)):
      next_num = int(input("Enter the next element: "))
      my_arr[x] = next_num
     

  print(sum(my_arr))
      
      

simpleArraySum()
