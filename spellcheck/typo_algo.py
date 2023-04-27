import string

def likely_typo_obj_maker():
    with open("typo_data.txt") as f:
        file_data = [line.strip() for line in f]

    key_str = string.ascii_lowercase + string.digits
    likely_typo_obj = dict()

    for i, char in enumerate(key_str):
        likely_typo_obj[char] = file_data[i]

    return likely_typo_obj


def inclusion_set_compiler(base_word, char, i, num_inclusions, set, training_data, likely_typo_obj, mod_string):
    if not char or num_inclusions == 0:
        return

    dupword = mod_string[:i] + mod_string[i] + mod_string[i:]
    set.add(dupword) # base letter is duplicated
    inclusion_set_compiler(base_word, base_word[i + 1] if i < len(base_word) - 1 else None, i + 1, num_inclusions, set, training_data, likely_typo_obj, dupword)

    for typo_letter in likely_typo_obj[char]:
        leftword = mod_string[:i] + typo_letter + mod_string[i + 1:]
        rightword = mod_string[:i - 1] + typo_letter + mod_string[i:]
        # rightword = (mod_string[:i] if i > 0 else "") + typo_letter + mod_string[i:]
        print(leftword)
        print(rightword)
        set.add(leftword) # extra letter is to the left of the base letter
        set.add(rightword) # extra letter is to the right of the base letter
        inclusion_set_compiler(base_word, base_word[i + 2] if i < len(base_word) - 2 else None, i + 2, num_inclusions - 1, set, training_data, likely_typo_obj, leftword)
        inclusion_set_compiler(base_word, base_word[i + 2] if i < len(base_word) - 2 else None, i + 2, num_inclusions - 1, set, training_data, likely_typo_obj, rightword)


def letter_excluder(base_word, mod_string, index, level, training_data):
    if level == 0 or index > len(mod_string) - 1:
        return

    sliced_string = mod_string[:index] + mod_string[index + 1:]
    training_data[sliced_string] = base_word
    training_data[mod_string] = base_word

    letter_excluder(base_word, sliced_string, index, level - 1, training_data)
    letter_excluder(base_word, mod_string, index + 1, level, training_data)


def typo_setter(base_word, num_exclusions, num_inclusions, training_data):
    num_exclusions = min(num_exclusions, len(base_word))
    num_inclusions = min(num_inclusions, len(base_word))

    likely_typo_obj = likely_typo_obj_maker()
    
    mod_string = base_word

    inclusion_string_set = set()
    print(inclusion_string_set)
    print(len(inclusion_string_set))

    for i, char in enumerate(base_word):
        inclusion_set_compiler(base_word, char, i, num_inclusions, inclusion_string_set, training_data, likely_typo_obj, base_word)


    for mod_string in inclusion_string_set:
        letter_excluder(base_word, mod_string, 0, num_exclusions, training_data)

    return training_data


print(len(typo_setter("ant", 3, 3, {})))