mi_bool = 4 < 5 > 3
print(mi_bool)

mi_bool = 4 < 5 and 5 > 3
print(mi_bool)

texto = "La casa de los Andes"
mi_bool = ('casa' in texto) or ('home' in texto)
print(mi_bool)

mi_bool = 'a' != 'a'
print(f"'a' != 'a' -> {mi_bool}")

mi_bool = not ('a' != 'a')
print(f"not ('a' != 'a') -> {mi_bool}")
