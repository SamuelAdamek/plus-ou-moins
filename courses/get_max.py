numbers = [15,67,12,78,89.3]
def get_max(numbers:list[float]) -> float:
    result = numbers[0]
    for number in numbers:
        if number > result :
            result = number
    return result


print(get_max(numbers)) # 89.3