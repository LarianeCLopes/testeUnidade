from datetime import date

def calculaIdade (nasc):
    today = date.today()

    try:
        aniversario = nasc.replace(year = today.year)
    except ValueError:
        aniversario = nasc.replace(year = today.year, moth = nasc.moth + 1, day = 1)

    if aniversario > today:
        return today.year - nasc.year - 1
    else:
        return today.year - nasc.year 

print(calculaIdade(date(l, 5, 1999)))
        