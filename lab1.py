# Esercizio 01.2.1
# Scrivere una frase di inaugurazione delle esercitazioni del corso di informatica.

print("Benvenuti al corso di Informatica!")


# Esercizio 01.2.2
# Stampa la somma dei primi 10 numeri interi positivi

somma = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10

print('La somma dei primi 10 interi vale', somma)


# Esercizio 01.2.3
# Stampa il prodotto dei primi 10 numeri interi positivi

prodotto = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

print('Il prodotto dei primi 10 interi vale', prodotto)

# Esercizio 01.2.4
# Scrivere un nome con lettere grandi
#
print("****   *****  *   *")
print("*  **  *      **  *")
print("****   ****   * * *")
print("*  **  *      *  **")
print("****   *****  *   *")

# Esercizio 01.2.5
# Scrivete il vostro nome, in colonna

print('J')
print('o')
print('h')
print('n')

# Esercizio 01.2.6
# Saldo di un conto corrente bancario

balance = 1000

#  The balance after year one.
balance = balance + balance * 0.05
print('After year 1, the balance is', balance)

#  The balance after year two.
balance = balance + balance * 0.05
print('After year 2, the balance is', balance)

#  The balance after year three.
balance = balance + balance * 0.05
print('After year 3, the balance is', balance)

# Esercizio 01.2.7
# Name in a box.
#
print("+-----+")
print("| Ben |")
print("+-----+")

# Esercizio 01.2.8
# Display an animal speaking a greeting.
#
print(" /\\_/\\    ________________")
print("( o o )  /                \\")
print("==_Y_== < Computer Science >")
print("  '-'    \\________________/")

# Esercizio 01.2.9
# Un codice alfanumerico lungo 16 caratteri che alterni le stringhe “abcd” e “1234”

# l'argomento end='' sopprime il carattere di a-capo, permettendo di stampare gli elementi successivi sulla stessa riga
print('abcd', end='')
print('1234', end='')
print('abcd', end='')
print('1234', end='')
print()

# Esercizio 01.2.10
# Scacchiera 5x5

riga_dispari = '01010'
riga_pari = '10101'

print(riga_dispari) #1
print(riga_pari) #2
print(riga_dispari) #3
print(riga_pari) #4
print(riga_dispari) #5

# Esercizio 01.2.11
# 100 simboli '-'

print('-' * 100)

# Esercizio 01.2.12
# 100 simboli '0'

print('0' * 100)

# Attenzione: usare '0' come stringa e non '0' come numero
# Sarebbe errato scrivere:
# print(0 * 100)
# Perché? cosa stamperebbe?

# Esercizio 01.2.13
# Fibonacci(4)

fib1 = 1
fib2 = 1
fib3 = fib1 + fib2
fib4 = fib2 + fib3

print(fib4)

# Esercizio 01.2.14
# Fibonacci(1...4)

fib1 = 1
print(fib1)

fib2 = 1
print(fib2)

fib3 = fib1 + fib2
print(fib3)

fib4 = fib2 + fib3
print(fib4)

# Esercizio 01.2.15
# Frase di chiusura

esercizi_totali = 15
esercizi_risolti = 14
percentuale = esercizi_risolti / esercizi_totali * 100
saluto = 'Arrivederci'

print('*' * (len(saluto) + 6))
print('**', saluto, '**')
print('*' * (len(saluto) + 6))

print('Esercizi risolti', percentuale, '%')
