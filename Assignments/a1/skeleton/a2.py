import random
from conversion import *


print("========== to_centigrade ==========")
cur = int(input("INPUT Fahrenheit: "))
print(f"Fahrenheit : {cur}")
cur = to_centigrade(cur)
print(f"Centigrade : {cur:.2f}\n")


print("========== to_fahrenheit ==========")
cur = int(input("INPUT Centigrade: "))
print(f"Centigrade : {cur}")
cur = to_fahrenheit(cur)
print(f"Fahrenheit : {cur:.2f}\n")

print("========== centigrade_to_kelvin ==========")
cur = int(input("INPUT Centigrade: "))
print(f"Centigrade : {cur}")
cur = centigrade_to_kelvin(cur)
print(f"Kelvin : {cur:.2f}\n")

print("========== fahrenheit_to_kelvin ==========")
cur = int(input("INPUT Fahrenheit: "))
print(f"Fahrenheit : {cur}")
cur = fahrenheit_to_kelvin(cur)
print(f"Kelvin : {cur:.2f}\n")

print("========== to_kermits ==========")
H = int(input("INPUT Hour : "))
H = int(input("INPUT Minute : "))
H = int(input("INPUT Second : "))
print(f"Hour : {H:02}")
print(f"Minute : {M:02}")
print(f"Second : {S:02}")
cur = to_kermits(H, M, S)
print(f"Kermits : {cur}\n")
