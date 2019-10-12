import random

int_dict = {
    1: 'a',
    2: 'e',
    3: 'i',
    4: 'o',
    5: 'u',
}

char_dict = {
    'a': u'\u3042',
    'e': u'\u3048',
    'i': u'\u3044',
    'o': u'\u304A',
    'u': u'\u3046',
}

# for key in char_dict:
#     print(char_dict[key])

random_int = random.randint(1, 5)
print(str(char_dict.get(int_dict.get(random_int))) + "\n")
answer_option = [int_dict.get(random_int)]
x = 0
while x < 2:
    z = random.randint(1,5)
    if answer_option.count(int_dict.get(z)) < 1:
        answer_option.append(int_dict.get(z))
        x += 1
while len(answer_option) > 0:
    z = random.randint(0, len(answer_option) - 1)
    print(answer_option[z])
    answer_option.pop(z)
