# write your program here
def complementary_letter(letter):
    if letter == 'A':
        return 'T'
    elif letter == 'T':
        return 'A'
    elif letter == 'C':
        return 'G'
    elif letter == 'G':
        return  'C'
    else:
        return 'N'

def complementary_strand(strand):
    letters = list(strand)
    return ''.join([complementary_letter(l) for l in letters])

strand = input()
print(complementary_strand(strand))
