def intersperse():
    sen1 = "This is a test"
    sen2 = "Of the emergency broadcast system."
    lst1 = sen1.split(" ")
    lst2 = sen2.split(" ")
    finalList = []
    count1 = 0
    count2 = 0
    i = 0
    if len(sen1) > len(sen2):
        while lst2 != []:
            i+=1
            if i%2 != 0:
                word = lst1.pop(0)
                finalList.append(word)
            else:
                word = lst2.pop(0)
                finalList.append(word)
        for i in range(len(lst1)):
            finalList.append(lst1[i])
    elif len(sen2) > len(sen1):
        while lst1 != []:
            i+=1
            if i%2 != 0:
                word = lst1.pop(0)
                finalList.append(word)
            else:
                word = lst2.pop(0)
                finalList.append(word)
        for i in range(len(lst2)):
            finalList.append(lst2[i])
    else:
        for i in range(len(sen1) + len(sen2)):
            i+=1
            if i%2 != 0:
                word = lst1.pop(0)
                finalList.append(word)
            else:
                word = lst2.pop(0)
                finalList.append(word)
    finalString = " ".join(finalList)
    return finalString
    
def main():
    print(intersperse())
main()

