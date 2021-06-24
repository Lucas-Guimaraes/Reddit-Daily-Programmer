#https://www.reddit.com/r/dailyprogrammer/comments/y5sox/8132012_challenge_88_easy_vigen%C3%A8re_cipher/

#Initial function
def vignere_cipher(key1, key2):
    #Makes keys uppercase, len for range, list for browsing
    key1 = key1.upper()
    key2 = key2.upper()
    key_len = len(key1)
    key1_lst = list(key1)
    key2_lst = list(key2)
    
    vignere = ''
    
    for i in range(key_len):
        #Gets total number
        total = ord(key1_lst[i]) + ord(key2_lst[i]) - 65
        
        #If the total is above Z, minus by 26
        if total > 90:
            total -= 26
        vignere += chr(total)
        
    #Return final vignere
    return vignere

print(vignere_cipher('GLADOSGLADOSG', 'THECAKEISALIE'))
raw_input()