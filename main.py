a = 24  #soviele Stunden hat der Tag
b = 365.25 # Tage hat das Jahr durchschnittlich
c = "Hallo Python"
d = 1
NiemandSagtNein = False
[a, b, d] #RandomListe

z = 5

def äußere_funktion():
    z = 30 # Nicht-lokale Variable

    def innere_funktion():
        nonlocal z
        z = 10
        print("Wert von z in der inneren Funktion:", z)

    innere_funktion()
    print("Wert von z in der äußeren Funktion:", z)

äußere_funktion()
print("Wert von z im globalen Bereich:", z)

print(len([a, b, d]))#Gibt die länge eines Objektes wieder

if type(z) is int:#Bestimmt den Datentyp eines Objektes
    print("z ist ein Ganzzahlwert")

print(sorted([a, b, d]))#sortiert eine Liste
print(min([a, b, d]))# Gibt das Minimum zurück
print(max([a, b, d]))# Gibt das Maximum zurück

print("Wie Groß bist du?")
Größe = float(input("Gib deine Größe an: "))
print("Du bist {0} Groß".format(Größe))
Größeint = int(Größe)
print("Du bist {0} Groß".format(Größeint))

print(isinstance(Größeint, float))