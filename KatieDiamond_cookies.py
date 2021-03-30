# this program is meant to calculate a recipe based on the inputted amount of cookies you want to make!
# introduce the recipe
print('This was written by Katie Diamond, who\'s in your MW 6pm SDEV140 class.')
print('Hello! Here is the original recipe which is for 48 cookies:')
print('1.5 cups of sugar;')
print('1 cup of butter;')
print('2.75 cups of flour')
# get input of the amount of cookies the user wants to bake
cookieAmount = int(input('Please enter the amount of cookies you would like to bake, as a whole number:'))
# confirm
print(f'It sounds like you want to bake {cookieAmount} cookie(s).')
print('To do that, you will need to use the following ingredients:')
# calculations, divide everything by 48 to find out the amount of one cookie then
# multiply by the amount of cookies inputted to find the total amount of ingredients.
sugarOne = 1.5 / 48
butterOne = 1 / 48
flourOne = 2.75 /48
# more calculations by inputted amount
sugarAllCookies = sugarOne * cookieAmount
butterAllCookies = butterOne * cookieAmount
flourAllCookies = flourOne * cookieAmount
# print to confirm everything is clear.
print(f'The amount of sugar you want to use is {sugarAllCookies:.1f} cup(s).')
print(f'The amount of butter you want to use is {butterAllCookies:.1f} cup(s).')
print(f'The amount of flour you want to use is {flourAllCookies:.1f} cup(s).')