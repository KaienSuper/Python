def golden_ratio(num):
    num_fib = [1, 1]
    for i in range(2, num + 2):
        num_fib.append(num_fib[i-1] + num_fib[i-2])
    print(num_fib[num]/num_fib[num-1])
    print(num_fib)
golden_ratio(4)