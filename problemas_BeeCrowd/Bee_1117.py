avaliacoes = 0

nota = 0

media_semestr = 0

while avaliacoes != 2:
    nota = float(input())
    
    if( nota >= 0 and nota <= 10):
        media_semestr += nota / 2
        avaliacoes = avaliacoes + 1
    
    else:
        print("nota invalida")
    
print("media = %.2f"%(media_semestr))