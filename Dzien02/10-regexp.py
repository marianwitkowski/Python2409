
# Wyrażenie regularne
import re

"""

k...a - wyraz na dokładnie 5 znaków, zaczyna się od "k" i kończy na "a"
Ma.*k - zaczyna się od "Ma" i konczy na "k" z dowolną liczba znaków pomiędzy (w tym zero)
Ma.+k - zaczyna się od "Ma" i konczy na "k" z liczba znaków >0
Ma?k - zaczyna się od "Ma" i konczy na "k" z liczba znaków pomiędzy 0 lub 1

^[0-9]{2}-[0-9]{3}$ - kod pocztowy

[0-9]  = \d
\D = nie cyfry
\s = znaki białe
\S - inne niż  znaki białe
\w - [0-9A-Za-z_]
\W - inne niż [0-9A-Za-z_]

"""
txt = "Mały Marek machał makatką trzymając trzy piwa"
result = re.findall("ma[a-z]{0,}k", txt.lower())
print(result)

txt = "01-123"
result = re.match("^[0-9]{2}-[0-9]{3}$", txt)
print(result)

txt = "Kwota do zaplaty 1234,56PLN, termin 7 dni. Wygenerowana 13:33"
result = re.findall("\d", txt)
print(result)
result = re.findall("\d+", txt)
print(result)

txt = "  Mały\r\n Marek\tmachał \fmakatką trzymając trzy piwa    "
#txt.replace(" ","*").replace("\t","*").replace("\r","*")
txt = re.sub("\s","*", txt, 4)
print(txt)