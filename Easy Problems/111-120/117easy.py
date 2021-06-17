#https://www.reddit.com/r/dailyprogrammer/comments/16jiuq/011413_challenge_117_easy_hexdump_to_ascii/
#https://stackoverflow.com/questions/8088375/how-do-i-convert-a-single-character-into-its-hex-ascii-value-in-python
#This has a complementary file that runs with it titled '117easytest.txt'

def hexdump_to_ascii(file):
    #This opens the text file, and then makes each part into a list
    with open(file, 'rb') as data:
        byte = data.read()
    byte_list = [[b for b in byte[i:i + 16]] for i in range(0, len(byte), 16)]
    #print(byte_list)
    
    #This enumerates the entire byte_list, convert them to their proper hexdump, and then print them
    for i, line in enumerate(byte_list):
        temp_line = '%08x' % i
        print(temp_line),
        for b in line:
            hexy = b.encode("hex") if b.isalpha() else '%02x' % ord(b)
            hexy_2 = ''
            for h in hexy: 
                if h.isalpha():
                    hexy_2 += h.upper()
                else:
                    hexy_2 += h
            print(hexy_2),
        print
        
file_name = '117easytest.txt'
hexdump_to_ascii(file_name)
raw_input()