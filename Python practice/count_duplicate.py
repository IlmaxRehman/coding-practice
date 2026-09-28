def find_duplicate(numbers):
    duplicate = []
    seen = set()
    for n in numbers:
        if n in seen:
            duplicate.append(n)
        else:
            seen.add(n)
    return duplicate

print(find_duplicate([4, 7, 2, 9, 7, 4, 1]))