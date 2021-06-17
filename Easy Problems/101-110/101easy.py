# https://www.reddit.com/r/dailyprogrammer/comments/10l8ay/9272012_challenge_101_easy_nonrepeating_years/

#This program checks for any repeating digits of a year in a range

def non_repeating_years(year1, year2):
    temp_year = year1
    nrp_lst = []
    #Temp Year is used to iterate over the current year
    while temp_year <= year2:
        str_year = str(temp_year)
        #Checks if the len of unique digits is the same as regular digits
        if len(set(str_year)) == len(str_year):
            nrp_lst.append(temp_year)
        temp_year += 1

    return nrp_lst

def year_inputs():
    first_check = True
    while first_check:
        first = raw_input("Please put in your first year: \n")
        if first.isdigit():
            first = int(first)
            first_check = False
    
    second_check = True
    while second_check:   
        second = raw_input("Please put in your second year: \n")
        if second.isdigit():
            second = int(second)
            if second > first:
                second_check = False
        
    print(non_repeating_years(first, second))

year_inputs()
print("\n~*~----------------~*~\n")
raw_input("Press enter to exit.")

#Test cases:
#print(non_repeating_years(1980, 1987))
#print(non_repeating_years(1909, 1910))
#print(non_repeating_years(1000, 2013))
