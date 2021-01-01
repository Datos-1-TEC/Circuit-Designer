Resist = ['R3', 'R1', 'R5', 'R2', 'R6', 'R4']

for i in range(len(Resist)):

    tmp = Resist[i]
    j = i-1 # stop index
    while (j > -1 and Resist[j] > tmp):
        Resist[j:j+2] = tmp,Resist[j] #swap places
        j -= 1
print(Resist)