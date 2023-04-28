require 'set'


def inclusion_set_compiler(base_word, char, i, num_inclusions, set, training_data, likely_typo_obj, mod_string, duplicate_char_bool=true)
    
    return if !char || num_inclusions == 0

    if (duplicate_char_bool)
        dupword = mod_string[0...i] + mod_string[i] + mod_string[i..-1]
        set.add(dupword) # base letter is duplicated
        inclusion_set_compiler(base_word, base_word[i + 1], i + 1, num_inclusions, set, training_data, likely_typo_obj, dupword, false)
    end

    likely_typo_obj[char].each_char do |typo_letter|
        leftword = mod_string[0...i] + typo_letter + mod_string[i + 1..-1]
        rightword = mod_string[0..i] + typo_letter + mod_string[i..-1]
        set.add(leftword) #extra letter is to the left of the base letter
        set.add(rightword) #extra letter is to the right of the base letter
        inclusion_set_compiler(base_word, base_word[i + 2], i + 2, num_inclusions - 1, set, training_data, likely_typo_obj, leftword)
        inclusion_set_compiler(base_word, base_word[i + 2], i + 2, num_inclusions - 1, set, training_data, likely_typo_obj, rightword)
    end

end

def letter_excluder(base_word, mod_string, index, level, training_data) 
    return if level == 0 || index > mod_string.length - 1
    sliced_string = mod_string.dup
    sliced_string.slice!(index)
    training_data[sliced_string] = base_word
    training_data[mod_string] = base_word

    letter_excluder(base_word, sliced_string, index, level - 1, training_data)
    letter_excluder(base_word, mod_string, index + 1, level, training_data)
end




def typo_setter(base_word, num_exclusions, num_inclusions, likely_typo_obj, training_data)

    num_exclusions = base_word.length if num_exclusions > base_word.length
    num_inclusions = base_word.length if num_exclusions > base_word.length

    mod_string = base_word

    inclusion_string_set = Set.new()

    i = 0
    while i < base_word.length
        char = base_word[i]
        inclusion_set_compiler(base_word, char, i, num_inclusions, inclusion_string_set, training_data, likely_typo_obj, base_word)
        i += 1
    end

    inclusion_string_set.each { |mod_string| letter_excluder(base_word, mod_string, 0, num_exclusions, training_data)}

    training_data
end




