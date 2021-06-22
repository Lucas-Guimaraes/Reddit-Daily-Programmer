# https://www.reddit.com/r/dailyprogrammer/comments/1e97ob/051313_challenge_125_easy_word_analytics/
#'125easy-test.txt' is a supplementary file

import re
import string

#Function #0, our 'root' function
#analyze_word_doc kicks all the other functions into motions
def analyze_word_doc(filename):
    file = open(filename, 'r')
    
    #file.seek(0) is used to refresh after each function
    word_total = word_count(file)
    file.seek(0)
    
    letter_total = letter_count(file)
    file.seek(0)
    
    symbol_total = symbol_count(file)
    file.seek(0)
    
    top_3_words = most_common_words(file)
    file.seek(0)
    
    top_3_letters = most_common_letter(file)
    file.seek(0)
    
    highest_starter = highest_paragraph_starter(file)
    file.seek(0)
    
    all_unique_words = unique_words(file) 
    file.seek(0)
    
    letters_not_included = unused_letters(file)
    file.seek(0)
    
    word_final = """    
    Word Total: {0}\n
    Letter Total: {1} \n
    Symbol Total: {2} \n
    Top 3 Words: {3} \n
    Top 3 Letters: {4} \n
    Highest Paragraph Starter: {5} \n
    All Unique Words: {6} \n
    Letters Not Included: {7}""".format(word_total, letter_total, symbol_total, top_3_words, top_3_letters, highest_starter, all_unique_words, letters_not_included)
    
    return word_final
    
    #return word_total, letter_total, symbol_total, top_3_words, top_3_letters, highest_starter, all_unique_words, letters_not_included
    
    
    
#returns the word count of the file
#Function #1
def word_count(file):
    word_count = 0

    for line in file.readlines():
        temp_line = line
        temp_line = ''.join(temp_line)
        temp_line = re.sub("[^a-zA-Z ]+", "", temp_line)
        line_split = temp_line.split()
       
        for word in line_split:
            word_count += 1
    
    return word_count
    
    
#returns the letter count of the file
#Function #2
def letter_count(file):
    letter_count = 0
    
    for line in file.readlines():
        for letter in line:
            if letter.isalpha():
                letter_count += 1
    return letter_count


#returns the symbol count of the file
#Function #3
def symbol_count(file):
    symbol_count = 0
    
    for line in file.readlines():
        for symbol in line:
            if symbol.isalpha() == False and symbol != ' ' and symbol != '\n':
                symbol_count += 1
    return symbol_count


#top 3 most common words
#Function #4
def most_common_words(file):
    temp_common_dict = {}
    common_words_dict = {}
    word_list = []
    temp_file = file.readlines()  
    
    
    for line in temp_file:
        temp_line = line
        temp_line = ''.join(temp_line)
        temp_line = re.sub("[^a-zA-Z ]+", "", temp_line)
        every_word = temp_line.split()
        
        for word in every_word:
            word_list.append(word)
    
    
    for word in word_list:
        if word not in temp_common_dict:
            temp_common_dict[word] = 1
        else:
            temp_common_dict[word] += 1


    for key, value in temp_common_dict.items():
        common_words_dict[value] = key
    
    biggest_wc = 0
    second_biggest_wc = 0
    third_biggest_wc = 0
    
    
    for key, value in common_words_dict.items():
        if int(key) > biggest_wc:
            biggest_wc = int(key)
    biggest_word = common_words_dict.get(biggest_wc)
    
    
    for key, value in common_words_dict.items():
        if int(key) > second_biggest_wc and value != biggest_word:
            second_biggest_wc = int(key)
    second_biggest_word = common_words_dict.get(second_biggest_wc)
    
    
    for key, value in common_words_dict.items():
        if int(key) > third_biggest_wc and value != biggest_word and value != second_biggest_word:
            third_biggest_wc = int(key)
    third_biggest_word = common_words_dict.get(third_biggest_wc)
    
    
    return biggest_word, second_biggest_word, third_biggest_word
    
    
#top 3 most common letters
#Function #5
def most_common_letter(file):
    common_letter_dict = {}
    temp_file = file.readlines()
    common_letter_dict_comp = {}
    letter_list = []
    
    for line in temp_file:
        for letter in line:
            if letter.isalpha():
                if letter in letter_list:
                    common_letter_dict[letter] += 1
                else:
                    common_letter_dict[letter] = 1
                    letter_list.append(letter)
                    
    
    for key, value in common_letter_dict.items():
            common_letter_dict_comp[value] = key
    
    biggest_lc = 0
    second_lc = 0
    third_lc = 0
    for key, value in common_letter_dict_comp.items():
        if int(key) > biggest_lc: #check if
            biggest_lc = int(key)
    most_used_letter = common_letter_dict_comp.get(biggest_lc)
    
    for key, value in common_letter_dict_comp.items():
        if int(key) > second_lc and value != most_used_letter:
            second_lc = key
    second_used_letter = common_letter_dict_comp.get(second_lc)
    
    for key, value in common_letter_dict_comp.items():
        if int(key) > third_lc and value != most_used_letter and value != second_used_letter:
            third_lc = key
    third_used_letter = common_letter_dict_comp.get(third_lc)
    
    return most_used_letter, second_used_letter, third_used_letter
    

#highest word to start a new paragraph. new paragraphs are via '\n'
#Function #6
def highest_paragraph_starter(file):
    paragraphs = file.readlines()
    paragraphs = ''.join(paragraphs)
    paragraphs = paragraphs.split("\n\n")
    paragraph_dict_temp = {}
    paragraph_dict = {}
    
    
    for paragraph in paragraphs:
        starter = True
        words = paragraph.split(' ')
        for word in words:
            if starter:
                starter = False
                if word in paragraph_dict_temp:
                    paragraph_dict_temp[word] += 1
                else:
                    paragraph_dict_temp[word] = 1
            else:
                break
                
    for key, value in paragraph_dict_temp.items():
        paragraph_dict[value] = key
    
    highest_starter_value = 0
    for key, value in paragraph_dict.items():
        if int(key) > highest_starter_value:
            highest_starter_value = key
    highest_opener = paragraph_dict.get(highest_starter_value)
    
    return highest_opener


#this checks all unique words in the file
#Function #7
def unique_words(file):
    unique_words_split = file.readlines()
    unique_list = []
    not_unique = []
    
    
    unique_words_split = ' '.join(unique_words_split)
    unique_words_split = unique_words_split.split("\n")
    
    unique_words_split = ''.join(unique_words_split)
    unique_words_split = unique_words_split.split(" ")

    
    for word in unique_words_split:
        temp_word = word
        temp_word = re.sub("[^a-zA-Z]+", "", temp_word)
        
        if temp_word in not_unique:
            pass
            
        else:
        
            if temp_word in not_unique:
                pass
                
            elif temp_word in unique_list:
                unique_list.remove(temp_word)
                not_unique.append(temp_word)
                
            else:
                unique_list.append(temp_word)
                
    return unique_list

#This file checks all the unused letters in the file.
#Function #8
def unused_letters(file):

    temp_file = file.readlines()
    
    list_of_letters = list(string.ascii_lowercase)

    for line in temp_file:
        for letter in line:
            if letter.isalpha():
                temp_letter = letter.lower()
                if temp_letter in list_of_letters:
                    list_of_letters.remove(temp_letter)
    return list_of_letters

print(analyze_word_doc('125easy-test.txt'))
raw_input()