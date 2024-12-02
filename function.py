def is_sorted(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

print(is_sorted([1,2,3,4,5,6,7]))
print(is_sorted([7,6,5,4,3,2,1]))
