# https://www.reddit.com/r/dailyprogrammer/comments/2zyipu/20150323_challenge_207_easy_bioinformatics_1_dna/

def dna_replicate(dna):
    other_side = ''
    dic = {' ': ' ',
           'A': 'T',
           'T': 'A',
           'C': 'G',
           'G': 'C'}
    for d in dna:
        other_side += dic[d]

    print(dna)
    print(other_side)


dna_replicate("A A T G C C T A T G G C")
raw_input("Press enter to exit.")