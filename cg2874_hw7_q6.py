def intersperse():
    sen1 = "I am writing words"
    sen2 = "My name is Clara, i was given it"
    lst1 = sen1.split(" ")
    lst2 = sen2.split(" ")
    finalList = []
    count1 = 0
    count2 = 0
    i = 0
    if len(lst1) > len(lst2):
        print("List 1 bigger")
        while count2 < len(lst2): 
            for i in range(len(lst1)+len(lst2)):
                if i%2 == 0:
                    finalList.append(lst1[count1])
                    count1+=1
                else:
                    finalList.append(lst2[count2])
                    count2+=1
                print(finalList)
        for i in range(len(lst1 - count1)):
            finalList.append(lst1[count1+i])
    elif len(lst2) > len(lst1):
        while count1 <= len(lst1): 
            if i%2 == 0:
                finalList.append(lst1[count1])
                count1+=1
            else:
                finalList.append(lst2[count2])
                count2+=1
                print("Count 1:", count1, "Count 2:", count2,finalList)
            i+=1
        for i in range(len(lst2 - count2)):
            finalList.append(lst2[count2+i])
    finalString = finalList.join(" ")
    return finalString
def main():
    print(intersperse())
main()
