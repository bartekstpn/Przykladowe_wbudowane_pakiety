inflacja1 = 1.59282448436825
inflacja2 = -0.453509101198007
inflacja3 = 2.32467171712441
kwota_kredytu = float(input("Podaj Kwotę kredytu: "))
oprocentowanie = float(input("Podaj oprocentowanie: "))
kwota_raty_kredytu = float(input("Podaj kwotę raty: "))

formula_do_obliczen = float((1 + ((inflacja1+oprocentowanie)/1200)) * kwota_kredytu - kwota_raty_kredytu)
formula_do_obliczen2 = float((1 + ((inflacja2+oprocentowanie)/1200)) * formula_do_obliczen - kwota_raty_kredytu)
formula_do_obliczen3 = float((1 + ((inflacja3+oprocentowanie)/1200)) * formula_do_obliczen2 - kwota_raty_kredytu)

print("Twoja pozostała kwota kredytu to:", str(round(formula_do_obliczen, 2)), "to: ", str(round(kwota_kredytu - formula_do_obliczen, 2)), "mniej niż w poprzednim miesiącu.")
print("Twoja pozostała kwota kredytu to:", str(round(formula_do_obliczen2, 2)), "to: ", str(round(formula_do_obliczen - formula_do_obliczen2, 2)), "mniej niż w poprzednim miesiącu.")
print("Twoja pozostała kwota kredytu to:", str(round(formula_do_obliczen3, 2)), "to: ", str(round(formula_do_obliczen2 - formula_do_obliczen3, 2)), "mniej niż w poprzednim miesiącu.")