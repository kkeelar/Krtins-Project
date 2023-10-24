

def birth():
     candles = [3, 2, 1, 3]
     max_1 = -1000000
     max_dict = []

     num_of_maxes = 0
     
     for index in range(len(candles)):
         if candles[index] > max_1:
               max_1 = candles[index]
     print("The max length is ", max_1)

     for element in candles:
          if element == max_1:
               num_of_maxes = num_of_maxes + 1

     print(num_of_maxes)
     return num_of_maxes
    
          
birth()
