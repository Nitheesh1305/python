#The function accepts the integer and squares it, at least according to type hints

def square(number: int) -> int:
    return number ** 2


print(square(3))
print(square(3.14))