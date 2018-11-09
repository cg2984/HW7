def sum_some(lower,upper,numbers):
    total = 0
    if numbers == []:
        return 0
    else:
        for i in range(len(numbers)):
            if numbers[i] >= lower and numbers[i] <= upper:
                total+=numbers[i];

        return total

def main():
    lower = 3
    upper = 3
    lst = [2,2,3,3,4,4]
    print(sum_some(lower, upper, lst))

main()
    
    
