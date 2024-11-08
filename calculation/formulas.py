def calorie_calculation_men(weight, height, age):
    return 10 * int(weight) + 6.25 * int(height) - 5 * int(age) + 5


def calorie_calculation_women(weight, height, age):
    return 10 * int(weight) + 6.25 * int(height) - 5 * int(age) - 161


def calorie_calculation_product(weight, calorie_in_100):
    return weight * calorie_in_100 / 100
