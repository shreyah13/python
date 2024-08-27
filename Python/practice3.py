def linear_search(adm, search_input):
    for i in range(adm):
        if adm[i] == search_input:
            return i
    return -1

size = int(input('Enter the size of the adm: '))
adm = []
for i in range(size):
