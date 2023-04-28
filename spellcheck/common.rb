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

    raw_common_data = File.open("common.txt")
    file_data = raw_common_data.readlines.map(&:chomp)
    likely_typo_obj = likely_typo_obj_maker

    training_data = {}
    file_data.each do |word|
        word_data = typo_setter(word.downcase, 1, 1, likely_typo_obj, {})
        p word_data
        training_data.merge(word_data)
    end

    data_file = File.open("training_data.txt", "w")
    p training_data
 
    training_data.each do |k,v|
        # data_file.write("#{[k,":"," ",v].join("")}\n")
        p "#{[k,":"," ",v].join("")}\n"
        data_file.write("bob")
    end

end

word_processer()