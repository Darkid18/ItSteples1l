result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b
try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15 ,8 : 4}
    for key in data:
            res = divider(key, data[key])
            result.append(res)

except (TypeError, IndexError, ValueError, ZeroDivisionError):
    print("Error")


print(result)
