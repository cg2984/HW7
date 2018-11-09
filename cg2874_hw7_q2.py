def avg (numbers) :
    total = 0
    for i in range(len(numbers)):
        total+=numbers[i]
    mean = total/len(numbers)
    return(mean)

def main():
    lst = [1,20,16,87,90,13,5]
    avg(lst)
    print(avg(lst))
main()
