'''
Mystery 1
  This takes a text input and compares it to "yes", "no" or "maybe". If the text input does equal one of those
  items then it returns the item that was typed in. If it not equal to any of those items, then the program will 
  return "unknown". 
  EXAMPLE
    def mystery1(x):
    for z in ["yes", "no", "maybe"]:
      if x == z:
        return z
      return "unknown"
    def main():
        val = input("Enter words")
        print(mystery1(val))
    main()
   OUTPUT:
   Enter words: yes
   yes
   
Mystery 2
  This program takes a list and puts the item in a string, speparated by commas. It then returns the string.
  EXAMPLE
    def mystery2(lst):
    acc = ""
      for item in lst:
          acc += item+", "
      return acc
    def main():
        names = ["Jenny", "Sarah", "Jorge", "Ana"]
        print(mystery2(val))
    main() 
   OUTPUT
   Jenny,Sarah,Jorge,Ana
   
Mystery 3
  This takes the beginning half of the items and adds them individually to the middle item, if they are numbers 
  then it will output the sum, and if it is strings then it will concatenate the string. 
  return "unknown". 
  EXAMPLE
    def mystery3(lst):
    i=0

    while i < len(lst) // 2:
      lst[i] += lst[i + len(lst) // 2]
      i+=1
    return lst[0:len(lst) // 2]
    def main():
        lst = [6,5,8,7,8]
        print(mystery3(val))
    main()
   OUTPUT
    [14,12]  
  
'''
