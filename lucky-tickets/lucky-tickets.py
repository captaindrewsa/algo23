
def count_of_lucky_ticket(ticket_lenght):
    max_count_of_sum = (ticket_lenght//2)*9 +1
    # print(max_count_of_sum)
    count_of_sums = [0 for _ in range(max_count_of_sum)]
    for elem in range(int("9"*(ticket_lenght//2))+1):
        summ = sum([int(digit) for digit in str(elem)])
        count_of_sums[summ]+=1
    
    result_count = sum([elem*elem for elem in count_of_sums])

    return result_count





print("Count of lucky tickets: ", count_of_lucky_ticket(19))