def reverse_pure(xs):
    lst2 = []
    lst3 = xs[:]
    for i in range(len(xs)):
        lst2.append(lst3.pop())
    return lst2
def reverse_mut(xs):
    for i in range(len(xs)):
        xs.insert(i,xs[(len(xs)-1)-i])
    for i in range(len(xs)//2):
        xs.pop()
    return xs
def main():
    mainList = [1,2,3,4]
    print(reverse_pure(mainList))
    print(reverse_mut(mainList))    
main()
