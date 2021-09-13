# https://www.reddit.com/r/dailyprogrammer/comments/2tr6yn/2015126_challenge_199_bank_number_banners_pt_1/

digits = [
    [" _ ", "| |", "|_|"]  # 0
    , ["   ", "  |", "  |"]  # 1
    , [" _ ", " _|", "|_ "]  # 2
    , [" _ ", " _|", " _|"]  # 3
    , ["   ", "|_|", "  |"]  # 4
    , [" _ ", "|_ ", " _|"]  # 5
    , [" _ ", "|_ ", "|_|"]  # 6
    , [" _ ", "  |", "  |"]  # 7
    , [" _ ", "|_|", "|_|"]  # 8
    , [" _ ", "|_|", " _|"]  # 9
]


def bank_num(num):
    str_0, str_1, str_2 = '', '', ''
    for i in str(num):
        str_0 += digits[int(i)][0]
        str_1 += digits[int(i)][1]
        str_2 += digits[int(i)][2]

    print(str_0)
    print(str_1)
    print(str_2)

print("Welcome to bank numbers!")
print("This will take your input, a number, and output it as a bank symbol.")
print("\n~*~--------~*~\n")

str_true = True
while str_true:
    n = raw_input("")
    if n.isdigit():
        bank_num(int(n))
    if n == 'Q' or n == 'q':
        break
raw_input("Press enter to exit")

#Test cases:
#bank_num(1234567890)