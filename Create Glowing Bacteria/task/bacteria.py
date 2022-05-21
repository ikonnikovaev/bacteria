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

# RESTRICTION_SITE = 'CTGCAG'
gfp_original = input().strip()
gfp_complementary = complementary_strand(gfp_original)
restriction_sites = input().split()

l_original = gfp_original.find(restriction_sites[0])
r_original = gfp_original.rfind(restriction_sites[1])
print(gfp_original[l_original + 1 : r_original + 1])

l_complementary = gfp_complementary.find(complementary_strand(restriction_sites[0]))
r_complementary = gfp_complementary.find(complementary_strand(restriction_sites[1]))
print(gfp_complementary[l_complementary + 5 : r_complementary + 5])

'''
first_strand, second_strand = input().split()
i = first_strand.find(RESTRICTION_SITE)
print(first_strand[:i + 1], first_strand[i + 1:])
j = second_strand.find(complementary_strand(RESTRICTION_SITE))
print(second_strand[:j + 5], second_strand[j + 5:])
'''
