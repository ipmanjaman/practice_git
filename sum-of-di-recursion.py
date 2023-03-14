def recur_sum(num):
    if num < 0:
        return "Positive Number only"
    elif num == 0:
        return 0
    else:
        return (num%10) + (recur_sum(num//10))
    
print(recur_sum(23445))