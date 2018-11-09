def indices(needle, haystack):
    pos = []
    for i in range(len(haystack)):
        if needle == haystack[i]:
            pos.append(i)
    return pos
def main():
    num = 7
    lst = [1,7,7,6]
    print(indices(num,lst))
main()
