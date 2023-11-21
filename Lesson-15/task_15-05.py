def number_in_english(number):
    num_1 = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", 'twelve', 'thirteen',
             'fourteen', 'sixteen', 'seventeen', "eighteen", "nineteen"]
    num_2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
             "eighty", "ninety", "hundred"]
    if number < 20:
        return num_1[number]
    elif number >= 20 and number < 100:
        return num_2[int(str(number)[0])-2] + " " + num_1[int(str(number)[1])]
    elif number >= 100:
        result = num_1[number//100] + " hundred" + " "
        result += num_2[int(str(number)[0])-2]
        return  result + " " + num_1[int(str(number)[1])]
print(number_in_english(20))
print(number_in_english(9))
print(number_in_english(35))
print(number_in_english(335))
