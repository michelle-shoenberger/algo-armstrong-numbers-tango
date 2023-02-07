
def find_armstrong_numbers(numbers):
    result = []
    if not isinstance(numbers, list):
        return result
    for number in numbers:
        # Determine sum of powers
        total = 0
        digits = [int(char) for char in str(number)]
        for digit in digits:
            total += digit**len(digits)
        # Check if equivalent to number
        if number == total:
            result.append(number)
    return result

#print(find_armstrong_numbers([371]))

# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])