def list_less_than_ten():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for element in a:
        if element < 5:
            b.append(element)
    print b
    
def divisors():
    number = int(raw_input("Enter a number: "))
    divisor_list = []
    divisor_range = list(range(1,number+1))
    for element in divisor_range:
        if number % element == 0:
            divisor_list.append(element)
    print divisor_list
    
def list_overlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    for element in a:
        if element in b:
            if element not in c:
                c.append(element)
    print c