def rlencode(string):
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphaList = alpha.split()
    alphaCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    tupList = []
    i = 0
    for i in range(len(string)):
        for j in range(len(alphaList)):
            if string[i] == alphaList[j]:
                alphaCount[j]+=1
                tup = (string[i], alphaCount[j])
                tupList.append(tup)
    return tupList

def main():
    letters = "aadccccaa"
    print(rlencode(letters))

main()
