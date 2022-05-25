numbers = []

# Сумма возрастов
for num1 in range(1, 14):
    for num2 in range(1, 14):
        for num3 in range(1, 14):
            sum = num1 + num2 + num3
            if sum == 13:
                x = list([num1, num2, num3])
                numbers.append(sorted(x))

#уникальный массив массивов
numbers = [list(x) for x in set(tuple(x) for x in numbers)]
#фильтрация где произведения чисел суммы равно 13
numbers = list(filter(lambda n: n[0] * n[1] * n[2], numbers))

compositions_of_numbers = []

for i in range(len(numbers)):
    number_of_duplication = 0
    for j in range(len(numbers)):
        nums1 = numbers[i]
        nums2 = numbers[j]

        composite1 = nums1[0] * nums1[1] * nums1[2]
        composite2 = nums2[0] * nums2[1] * nums2[2]

        if (composite1 == composite2):
            number_of_duplication += 1

        if (number_of_duplication > 1):
            compositions_of_numbers.append(nums1)
            break

#print(compositions_of_numbers)

for i in range(len(compositions_of_numbers)):
    for j in range(len(compositions_of_numbers[i])):
        if j == 0:
            continue
        if (compositions_of_numbers[i][j] != compositions_of_numbers[i][j-1] and compositions_of_numbers[i][j] > compositions_of_numbers[i][j-1]):
            break
        else:
            print("Первому ребенку", str(compositions_of_numbers[i][0]))
            print("Второму ребенку", str(compositions_of_numbers[i][1]))
            print("Третьему ребенку", str(compositions_of_numbers[i][2]))