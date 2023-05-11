require './typo_algo.rb'

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


def word_processer

    raw_common_data = File.open("1k_common.txt")
    file_data = raw_common_data.readlines.map(&:chomp)

    output_file = File.open("training_text.txt", "w")
    
    likely_typo_obj = likely_typo_obj_maker

    i = 1
    file_data.each do |word|
        p "processing #{i}/#{file_data.length}"
        i += 1

        next if word == ""
        word_data = typo_setter(word.downcase, 1, 1, likely_typo_obj, {})

        word_data.each do |k,v|
            next if k == ""
            output_file.write("#{[k,":"," ",v].join("")}\n")
        end
        system("clear")
    end



end

word_processer()