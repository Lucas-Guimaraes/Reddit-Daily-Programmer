# https://www.reddit.com/r/dailyprogrammer/comments/21w3lb/412014_challenge_156_easy_simple_decoder/

def decode_string(string):
    mod_str = ''
    #i_ascii = incorrect ascii
    #c_ascii = correct ascii
    for letter in string:
        i_ascii = ord(letter)
        c_ascii = i_ascii - 4
        mod_str += chr(c_ascii)
    return mod_str



print("Welcome to string decoder!")
print("This program takes one input: A string")
print("Afterwards, it will decode your message from that string.")
print("It only decodes by ascii values that are forwarded 4 spaces")
print("\n~*~----------------~*~\n")
str_decode = raw_input("Put your string to decode: \n")
print(decode_string(str_decode))
raw_input("\nPress Enter to exit.")

# print(decode_string("""Etvmp$Jsspw%%%%
# [e}$xs$ks%$]sy$lezi$wspzih$xli$lmhhir$qiwweki2$Rs{$mx$mw$}syv$xyvr$xs$nsmr
# mr$sr$xlmw$tvero2$Hs$rsx$tswx$er}xlmrk$xlex${mpp$kmzi$e{e}$xlmw$qiwweki2$Pix
# tistpi$higshi$xli$qiwweki$sr$xlimv$s{r$erh$vieh$xlmw$qiwweki2$]sy$ger$tpe}$epsrk
# f}$RSX$tswxmrk$ls{$}sy$higshih$xlmw$qiwweki2$Mrwxieh$tswx$}syv$wspyxmsr$xs$fi$}syv
# jezsvmxi$Lipps${svph$tvskveq$mr$sri$perkyeki$sj$}syv$glsmgi2$
# Qeoi$wyvi$}syv$tvskveq$we}w$&Lipps$[svph%%%&${mxl$7$%$ex$xli$irh2$Xlmw${e}
# tistpi$fvs{wmrk$xli$gleppirki${mpp$xlmro${i$lezi$epp$pswx$syv$qmrhw2$Xlswi${ls$tswx$lipps
# {svph$wspyxmsrw${mxlsyx$xli$xlvii$%%%${mpp$lezi$rsx$higshih$xli$qiwweki$erh$ws$}sy$ger$
# tspmxip}$tsmrx$syx$xlimv$wspyxmsr$mw$mr$ivvsv$,xli}$evi$nywx$jspps{mrk$epsrk${mxlsyx$ors{mrk-
# Irns}$xlmw$jyr2$Xli$xvyxl${mpp$fi$liph$f}$xlswi${ls$ger$higshi$xli$qiwweki2$>-"""))