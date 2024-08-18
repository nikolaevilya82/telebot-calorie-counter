def calorie_calculation_men(weight, height, age):
    return 10 * int(weight) + 6.25 * int(height) - 5 * int(age) + 5


def calorie_calculation_women(weight, height, age):
    return 10 * int(weight) + 6.25 * int(height) - 5 * int(age) - 161


# man = calorie_calculation_men(67, 175, 42)
# woman = calorie_calculation_women(55, 167, 35)
# print(f'for man {round(man)}, number of calories per day')
# print(f'for man {round(woman)}, number of calories per day')