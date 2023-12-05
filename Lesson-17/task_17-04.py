sequence = [1, 1]
def continue_fibonacci_sequence(sequence, n): 
    for i in range(n): 
        next_element = sequence[-1] + sequence[-2] 
        sequence.append(next_element)
    return sequence
sequence = continue_fibonacci_sequence(sequence, 5)
print(sequence)
#Начальный код не работал по той причине, что sequence, который вне функции и 
#sequence в функции это разные переменные