import math

print("Ingrese la velocidad final: ")
VF = float(input())
print("Ingrese la velocidad inicial: ")
VI = float(input())
print("Ingrese el tiempo transcurrido: ")
T = int(input())

A = (VF - VI) / T

print(f"\nLa velocidad final fue de: {VF}km/h \nLa velocidad inicial fue de: {VI}km/h \nEl tiempo transcurrido fue de: {T}s \nLa Aceleracion fue de: {A}m/s^2")