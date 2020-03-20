weight = input('How much do you weigh?:')
height = input('How tall are you? (In inches):')

bmi = int(703) * int(weight) / int(height)**2
print(bmi)

if bmi < int(18.5):
    print('You are underweight')
elif int(24.9 >= bmi >= 18.5):

    print('You are at a health weight')
elif int(29.9 >= bmi >= 25):

    print('You are slightly overweight')
elif int(34.0 >= bmi >= 30):

    print('You are obese')
elif bmi > int(35):
    print('You are extremely obese')