# write your program here
import string

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

RESTRICTION_SITE = 'CTGCAG'
strand = input()
print(strand)
print(complementary_strand(strand))
'''
first_strand, second_strand = input().split()
i = first_strand.find(RESTRICTION_SITE)
print(first_strand[:i + 1], first_strand[i + 1:])
j = second_strand.find(complementary_strand(RESTRICTION_SITE))
print(second_strand[:j + 5], second_strand[j + 5:])
'''
