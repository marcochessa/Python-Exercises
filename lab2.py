# Esercizio 02.1.1
# Calcoli con due numeri

a = 312
b = -27

somma = a + b
print('Somma', somma)

differenza = a - b
print('Differenza', differenza)

prodotto = a * b
print('Prodotto', prodotto)

media = somma / 2
print('Media', media)

distanza = abs(differenza)
print('Distanza', distanza)

massimo = max(a, b)
print('Massimo', massimo)

minimo = min(a, b)
print('Minimo', minimo)

# Esercizio 02.1.2
# Resistenze

# Per calcolare la resistenza totale dovrò calcolare I1, e poi R = E / I1

# Consideriamo il parallelo tra R2 e R3, con caduta di tensione V2.
# V2 = R2 * I2 e V2 = R3 * I3
# oppure I2 = V2/R2 e I3 = V2/R3

# La resistenza equivalente del parallelo tra R2 e R3 sarà
# R23 = V2 / (I2 + I3)
# sostituendo
# R23 = V2 / ( V2/R2 + V2/R3 ) = V2 / ( V2 * (1/R2+1/R3) )
# quindi (semplificando V2) R23 = 1 / (1/R2 + 1/R3)

# Considerando poi il collegamento di R1 "in serie", abbiamo che
# E = V1 + V2 = R1 * I1 + R23 * I1 (perché sarebbe R23 * (I2+I3), ma la corrente totale è I1)
# Ricavo I1 = E / (R1 + R23)
# Allora la resistenza totale sarà
# Rtot = E / I1 = R1 + R23


r1 = 100
r2 = 150
r3 = 300

# Per la lettura da tastiera, scommentare le righe seguenti:
# r1 = float(input('Valore di R1 (Ω): '))
# r2 = float(input('Valore di R2 (Ω): '))
# r3 = float(input('Valore di R3 (Ω): '))

# r23 è il parallelo tra r2 ed r3
r23 = 1 / (1 / r2 + 1 / r3)

# la resistenza equivalente è la serie tra r1 ed r23
r = r1 + r23

print('Resistenza totale', r, 'Ω')

# Esercizio 02.1.3
# Cifre

# Read a 5 digit integer and display it with one digit per row.

# OPTION 1: treat the number as a 5-character string

# Gather input from the user.
num = input("Enter a 5 digit integer: ")

# Display the result.
print(num[0])
print(num[1])
print(num[2])
print(num[3])
print(num[4])

# OPTION 2: use Division and Modulo of powers of 10

num = int(input("Enter a 5 digit integer: "))

print((num // 10000) % 10)
print((num // 1000) % 10)
print((num // 100) % 10)
print((num // 10) % 10)
print(num % 10)


# Esercizio 02.1.4
# Auto ibrida

COSTO_AUTO_NUOVA = 15000 # €
KM_PER_ANNO = 30000 # km
COSTO_CARBURANTE = 2.00 # €/l
EFFICIENZA = 12 # km/l
VALORE_RIVENDITA = 6000 # €

# NOTA: modificare il programma in modo che sia l'utente a inserire i valori delle costanti sopra definite

costo_km = COSTO_CARBURANTE/EFFICIENZA # €/km
costo_annuo = KM_PER_ANNO * costo_km # €/anno

costo_5_anni = COSTO_AUTO_NUOVA + 5 * costo_annuo - VALORE_RIVENDITA

print('Costo totale in 5 anni = ', costo_5_anni, '€')

# Esercizio 02.1.5
# Forza di Coulomb

from math import pi

# Define constants.
EPSILON = 8.854e-12

# Gather input from the user.
q1 = float(input("Enter the charge for particle 1 (C): "))
q2 = float(input("Enter the charge for particle 2 (C): "))
r = float(input("Enter the distance between (m): "))

# Compute the force.
f = (q1 * q2) / (4 * pi * EPSILON * r ** 2)

# Display the result.
print("The force is", f, "N")


# Esercizio 02.2.1
# Carrello

#  Print the first 3 letters of a string, followed by ..., followed by the
#  last 3 letters of a string.


# Initialize the string.
string = "Mississippi"

# Or... read the string from the user
#string = input('Enter a string:')

# NOTE: The string should have more than 6 characters
# What happens if it is shorter than 6 characters?
# What happens if it is shorter than 3 characters?

beginning = string[0:3]
ending = string[-3:]

# using sep='' to suppress the space between arguments
print(beginning, '...', ending, sep='')

# using f-strings:
print(f'{beginning}...{ending}')

# Esercizio 02.2.2
# Numero telefonico

# Display a phone number with nice formatting.

# Gather input from the user.
num = input("Enter a 10 digit phone number: ")

# Extract the parts of the number.
area_code = "(" + num[0:3] + ")"
formatted = area_code + " " + num[3:6] + "-" + num[6:10]

# Display the result.
print("The formatted number is:", formatted)

# Esercizio 02.2.3
# Allineamento

# Calcoli con due numeri, stampa in colonna

a = 312
b = -27

somma = a + b
differenza = a - b
prodotto = a * b
media = somma / 2
distanza = abs(differenza)
massimo = max(a, b)
minimo = min(a, b)

print('Somma      ', f'{somma:5d}')
print('Differenza ', f'{differenza:5d}')
print('Prodotto   ', f'{prodotto:5d}')
print('Media      ', f'{media:5.1f}')
print('Distanza   ', f'{distanza:5d}')
print('Massimo    ', f'{massimo:5d}')
print('Minimo     ', f'{minimo:5d}')

# Esercizio 02.2.4
# Emoji

# Ipotizziamo che le mie Emoji più frequenti siano le seguenti:
" 👍 🙂 😲 "

# Per conoscere il codice Unicode si può usare la funzione ord()
# ord('👍') --> 128077
# Nelle tabelle Unicode solitamente si usa il valore espresso in base 16
# che si può ottenere dalla funzione hex()
# hex(128077) --> '0x1f44d'
# o direttamente: hex(ord('👍')) --> '0x1f44d'

emoji1 = '👍'
rank1 = 4 # from https://home.unicode.org/emoji/emoji-frequency/
unicode1 = '1F44D' # from https://unicode-table.com/en/1F44D/
name1 = 'Thumbs Up Sign'

emoji2 = '🙂'
rank2 = 28 # from https://home.unicode.org/emoji/emoji-frequency/
unicode2 = '1F642' # from https://unicode-table.com/en/1F642/
name2 = 'Slightly Smiling Face'

emoji3 = '😲'
rank3 = 111 # from https://home.unicode.org/emoji/emoji-frequency/
unicode3 = '1F632' # from https://unicode-table.com/en/1F632/
name3 = 'Astonished Face'

print("Emoji 1", emoji1)
print(f'Posizione={rank1}, numero={unicode1}, nome={name1}')

print("Emoji 2", emoji2)
print(f'Posizione={rank2}, numero={unicode2}, nome={name2}')

print("Emoji 3", emoji3)
print(f'Posizione={rank3}, numero={unicode3}, nome={name3}')

# Esercizio 02.2.5
# Immatricolazioni

matricola1 = 'S301888'
matricola2 = 'S800123'

# tutte le matricole da studente in Ateneo iniziano con la stessa lettera, per cui possiamo ricavarla da uno qualunque dei due codici di matricola

lettera = matricola1[0]

valore1 = int(matricola1[1:])
valore2 = int(matricola2[1:])

primaMatricola = min(valore1, valore2)
secondaMatricola = max(valore1, valore2)

print(lettera + str(primaMatricola), sep='')
print(lettera + str(secondaMatricola), sep='')

