def to_number(word):
    number = 0
    for c in word:
        number += ord(c) - ord("A") + 1
    return number


def triangle_number(n):
    return int(0.5 * n * (n + 1))


triangle_numbers = [1]
triangle_words = 0
with open("p042_words.txt") as words_file:
    words = words_file.read().split(",")
    for word in words:
        number = to_number(eval(word))
        while number > triangle_numbers[-1]:
            triangle_numbers.append(triangle_number(len(triangle_numbers) + 1))
        if number in triangle_numbers:
            triangle_words += 1
print(triangle_words)