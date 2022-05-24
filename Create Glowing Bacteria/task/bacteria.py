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


file_name = input()
file = open(file_name)
lines = [line.strip() for line in file.readlines()]
plasmid_original = lines[0]
plasmid_restriction = lines[1]
gfp_original = lines[2]
gfp_restriction = lines[3].split()

p = plasmid_original.find(plasmid_restriction)
l = gfp_original.find(gfp_restriction[0])
r = gfp_original.rfind(gfp_restriction[1])

result = plasmid_original[:p + 1] + gfp_original[l + 1 : r + 1] + plasmid_original[p + 1:]
result = result.strip()
print(result)
print(complementary_strand(result))


'''

l_original = gfp_original.find(restriction_sites[0])
r_original = gfp_original.rfind(restriction_sites[1])
print(gfp_original[l_original + 1 : r_original + 1])

l_complementary = gfp_complementary.find(complementary_strand(restriction_sites[0]))
r_complementary = gfp_complementary.find(complementary_strand(restriction_sites[1]))
print(gfp_complementary[l_complementary + 5 : r_complementary + 5])
'''

