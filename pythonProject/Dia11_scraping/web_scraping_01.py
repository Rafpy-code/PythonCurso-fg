'''
requirements.txt
beautifulsoup4==4.9.3
requests==2.27.1
lxml==4.7.1
'''

import bs4
import requests

resultado = requests.get("https://escueladirecta-blog.blogspot.com/")
#print(resultado.text)
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
#print(sopa)
print('Titulo pestaña: ' + sopa.select('title')[0].getText())
#print(sopa.select('a'))
print("sopa.select('h3')[1]: " + sopa.select('h3')[1].getText())
#print(sopa.find(id="name"))
#print(sopa.find_all(class_="text"))

print('*' *5 + " Menú Principal " + '*' * 5)
menu = sopa.find_all("a")
for i in range(1, 6):
    if(menu[i+1].get('href') == ('')):
        continue
    print(f"*.- {menu[i+1].get('href')}")
print('*' * 20 + '\n')

# Extraer imagenes de una pagina web
print('*' * 5 + " Imagenes " + '*' * 5) 
resultado1 = requests.get('https://www.escueladirecta.com/courses/')
sopa1 = bs4.BeautifulSoup(resultado1.text, 'lxml')
imagenes = sopa1.select('.course-box-image')

for i in range(0, len(imagenes)):
    if(imagenes[i].get('src') == None):
        continue
    print(f'imagen: {imagenes[i]['src']}')
    # Extraer imagen a un archivo
    nombre_imagen = f"imagen_{i}"
    nombre_imagen = requests.get(sopa1.select('.course-box-image')[i].get('src'))
    f = open('D:\PROGRAMACION\PythonCurso-fg\pythonProject\Dia11_scraping\imagen_0.jpg', 'wb')
    f.write(nombre_imagen.content)
    f.close()
print('*' * 20)
