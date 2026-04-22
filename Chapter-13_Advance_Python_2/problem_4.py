def divisoble_by_5(n):
    return n % 5 == 0

l = [1, 5, 10, 12, 15, 20, 25]
divisible_by_5_list = filter(divisoble_by_5, l)
print(list(divisible_by_5_list)) 