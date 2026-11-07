all_numbers = list(range(0,37))

# Cabinets Mattroy
jeu_0_numbers = [12, 35, 3, 26, 0, 32, 15]
voisins_du_zero_numbers = [22, 18, 29, 7, 28, 12, 35, 3, 26, 0, 32, 15, 19, 4, 21, 2, 25]
orphelins_numbers = [1, 20, 14, 31, 9, 17, 34, 6]
tiers_du_cylindre_numbers = [27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33]
cabinets_mattroy_groups = [jeu_0_numbers, voisins_du_zero_numbers, orphelins_numbers, tiers_du_cylindre_numbers]
cabinets_mattroy_groups_names = ["Jeu 0", "Voisins du Zero", "Orphelins", "Tiers du Cylindre"]

# Red and Black
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [number for number in all_numbers if number not in red_numbers and not number == 0]
def get_number_colour(number):
    if number in red_numbers:
        return 'red'
    elif number in black_numbers:
        return 'black'
    elif number == 0:
        return 'green'
    
# Halfs
half_1st = list(range(1,19))
half_2nd = list(range(19,37))
def get_number_half(number):
    if number in half_1st:
        return '1st half'
    elif number in half_2nd:
        return '2nd half'

# Even and Odd
Even = []
Odd = []
for number in range(1,37):
    if number % 2 == 0:
        Even.append(number)
    elif number % 2 == 1:
        Odd.append(number)

# Dozens
dozen_1st = list(range(1,13))
dozen_2nd = list(range(13,25))
dozen_3rd = list(range(25, 37))
def get_number_dozen(number):
    if number in dozen_1st:
        return '1st dozen'
    elif number in dozen_2nd:
        return '2nd dozen'
    elif number in dozen_3rd:
        return '3rd dozen'

# Columns
column_1 = []
column_2 = []
column_3 = []
for number in range(1,37):
    if number % 3 == 1:
        column_1.append(number)
    elif number % 3 == 2:
        column_2.append(number)
    elif number % 3 == 3:
        column_3.append(number)