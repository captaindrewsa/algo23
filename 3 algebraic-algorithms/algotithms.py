
def itteration_pow(number, degree):
    output= number
    for _ in range(1,degree):
        output*=number
    return output
# print(itteration_pow(2,4))

def fibonacchi_recursion(n):
    if ( n > 2 ):
        return (fibonacchi_recursion(n-1) + fibonacchi_recursion(n-2))
    else:
        return 1
# print(fibonacchi_recursion(10))


def fibonaci_itteration(n):
    if (n <= 2):
        return 1
    x = 1
    y = 1
    ans = 0
    for i in range(2,n):
        ans = x + y
        x = y
        y = ans
    return ans
# print(fibonaci_itteration(10))

def search_for_prime_numbers(n):
    count = 1
    if n == 1:
        return 0
    if n == 2:
        return count
    
    for number in range(2,n+1):
        if number!=2 and number%2==0:
            continue
        if number!= 3 and number%3==0:
            continue
        if number!= 5 and number%5==0:
            continue
        
        tmp=0
        for divider in range(2,number):
            if number%divider==0:
                continue
            else:
                tmp+=1
        if tmp!=0:
            count+=1
        else:
            continue
    return count
# print(search_for_prime_numbers(25))
