

def typo_setter(base_word, num_exclusions, num_inclusions)

    num_exclusions = base_word.length if num_exclusions > base_word.length
    num_inclusions = base_word.length if num_exclusions > base_word.length
    
    training_data = Hash.new(base_word)
    mod_string = base_word

    "question"


    i = 0
    while i < base_word.length


    i += 1
    end



    letter_excluder(base_word, mod_string, 0, num_exclusions, training_data)

    training_data
end



def letter_excluder(base_word, mod_string, index, level, hash) 
    return if level == 0 || index > mod_string.length - 1
    sliced_string = mod_string.dup
    sliced_string.slice!(index)
    hash[sliced_string] = base_word
    hash[mod_string] = base_word

    letter_excluder(base_word, sliced_string, index, level - 1, hash)
    letter_excluder(base_word, mod_string, index + 1, level, hash)
end


