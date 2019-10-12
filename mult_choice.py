import random

int_dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e'
    }

char_dict = {
    'a': 'あ'
    'e': 'え'
    'i': 'い'
    'o': 'お'
    'u': 'う'
    }


y = random.randint(1, 5)
print(char_dict.get(int_dict.get(y)))
answer_option = [int_dict.get(y)]
print()
x = 0
while x < 2:
    z = random.randint(1,5)
    if answer_option.count(int_dict.get(z)) < 1:
        answer_option.append(int_dict.get(z))
        x += 1
while len(answer_option) > 0:
    z = random.randint(0, len(answer_option) - 1)
    print(answer_option.pop(z))
    
        
