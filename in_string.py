def check_vowels():
    name = input("ingrese un nombre:")
    has_a = ("a" in name.lower())
    has_e = ("e" in name)
    has_i = ("i" in name)
    has_o = ("o" in name)
    has_u = ("u" in name)
    print (f"Contiene a: {has_a}")
    print (f"Contiene e: {has_e}")
    print (f"Contiene i: {has_i}")
    print (f"Contiene o: {has_o}")
    print (f"Contiene u: {has_u}")
    # Código a implementar utilizando input.

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
