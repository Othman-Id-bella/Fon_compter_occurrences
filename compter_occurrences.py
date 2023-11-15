def compter_occurrences(chaine, caractere):
    return chaine.count(caractere)

chaine_test = "python programming"
caractere_test = "p"
occurrences = compter_occurrences(chaine_test, caractere_test)
print(f"Le caractère '{caractere_test}' apparaît {occurrences} fois dans la chaîne.")
