def likely_typo_obj_maker
    raw_typo_data = File.open("typo_data.txt")
    file_data = raw_typo_data.readlines.map(&:chomp)
    key_str = "abcdefghijklmnopqrstuvwxyz1234567890"
    likely_typo_obj = Hash.new()

    key_str.each_char.with_index do |char, i|
        likely_typo_obj[char] = file_data[i]
    end

    likely_typo_obj
end


def queue_maker(base_word, char, i, num_inclusions, queue, training_data, likely_typo_obj, mod_string)
    return if i > mod_string.length || num_inclusions == 0

    queue.push(base_word[0...i] + base_word[i] + base_word[i..-1]) # base letter is duplicated

    likely_typo_obj[char].each_char do |typo_letter|
        queue.push(base_word[0...i] + typo_letter + base_word[i..-1]) #extra letter is to the left of the base letter
        queue.push(base_word[0..i] + typo_letter + base_word[i + 1..-1]) #extra letter is to the right of the base letter
    end

    queue.each do |mod_string|
        queue_maker(base_word, base_word[i + 2], i + 2, num_inclusions - 1, training_data, mod_string)
    end

    queue_maker(base_word, base_word[i + 1], i + 1, num_inclusions, training_data, mod_string)
end




def typo_setter(base_word, num_exclusions, num_inclusions, training_data)

    num_exclusions = base_word.length if num_exclusions > base_word.length
    num_inclusions = base_word.length if num_exclusions > base_word.length

    likely_typo_obj = likely_typo_obj_maker()
    
    mod_string = base_word

    "question"

    queue = []

    i = 0
    while i < base_word.length
        char = base_word[i]

        queue_maker(base_word, char, i, num_inclusions, queue, training_data, likely_typo_obj, base_word)

        #make a function that 

        # queue.push(base_word[0...i] + base_word[i] + base_word[i..-1]) # base letter is duplicated

        # likely_typo_obj[char].each_char do |typo_letter|
        #     queue.push(base_word[0...i] + typo_letter + base_word[i..-1]) #extra letter is to the left of the base letter
        #     queue.push(base_word[0..i] + typo_letter + base_word[i + 1..-1]) #extra letter is to the right of the base letter
        # end


        # while queue.length > 0

        # end
        # outer loop iterates through each character
        # inner loop through the likely typo arr and produce the following variations
            # base letter is duplicated
            # extra letter is to the left of the base letter
            # extra letter is to the right of the base letter
        # each variation gets run through letter_excluder

        # each variation also needs to go through the inner loop again to account for multiple typos, controlled by num_inclusions

        "arnold"

        "aarnold" #
            

        i += 1
    end

    p queue

    # letter_excluder(base_word, mod_string, 0, num_exclusions, training_data)

    # training_data
end


typo_setter("arnold", 3, 3, {})



def letter_excluder(base_word, mod_string, index, level, training_data) 
    return if level == 0 || index > mod_string.length - 1
    sliced_string = mod_string.dup
    sliced_string.slice!(index)
    training_data[sliced_string] = base_word
    training_data[mod_string] = base_word

    letter_excluder(base_word, sliced_string, index, level - 1, training_data)
    letter_excluder(base_word, mod_string, index + 1, level, training_data)
end


