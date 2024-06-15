a = int(input("Inserisci il primo numero: 10"))
b = int(input("Inserisci il secondo numero: 20"))

if a == b:
    print("I numeri sono identici")
elif a > b:
    print("Il numero più grande tra i due è " + str(a))
else:
    print("Il numero più grande tra i due è " + str(b))