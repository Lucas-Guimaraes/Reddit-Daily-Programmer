#https://www.reddit.com/r/dailyprogrammer/comments/7b5u96/20171106_challenge_339_easy_fixedlength_file/

highest_salary = 0

for line in open("339easy.txt"):
    if line[:7] == "::EXT::":
        if line[7:10] == "SAL":
            salary = int(line[11:])
            if salary > highest_salary:
                highest_salary = salary
                highest_employee = current_employee
    else:
       current_employee = line[:20].strip()

print(highest_employee+", ${:,}".format(highest_salary))
raw_input("Press enter to exit.")