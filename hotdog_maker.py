import dni_generator as dni_maker
import requests
import random
import time

# Data (Retrieved from INE website
man_names = ["Antonio", "Jose","Manuel",  "Francisco", "David", "Juan", "Jose Antonio", "Javier", "Jose Luis", "Daniel",
             "Francisco Javier", "Jesus", "Carlos", "Alejandro", "Miguel", "Jose Manuel", "Rafael", "Pedro",
             "Miguel Angel","Angel", "Pablo", "Jose Maria", "Fernando", "Sergio", "Luis", "Jorge", "Alberto",
             "Juan Carlos", "Alvaro","Juan Jose", "Diego", "Adrian", "Raul", "Juan Antonio", "Ivan", "Enrique", "Ruben",
             "Ramon", "Vicente", "Oscar","Andres", "Joaquin", "Juan Manuel", "Santiago", "Eduardo", "Victor", "Mario",
             "Roberto", "Jaime", "Francisco Jose","Ignacio", "Marcos", "Alfonso", "Jordi", "Salvador", "Ricardo",
             "Emilio", "Hugo", "Guillermo", "Gabriel", "Julian","Julio", "Marc", "Tomas", "Jose Miguel", "Gonzalo",
             "Agustin", "Mohamed", "Jose Ramon", "Felix", "Nicolas", "Joan", "Martin", "Ismael", "Cristian", "Samuel",
             "Aitor", "Juan Francisco", "Josep", "Hector", "Mariano", "Domingo","Jose Carlos", "Alfredo", "Sebastian",
             "Iker", "Cesar", "Felipe", "Alex", "Lucas", "Jose Angel", "Jose Ignacio","Victor Manuel", "Luis Miguel",
             "Rodrigo", "Gregorio", "Jose Francisco", "Juan Luis", "Xavier", "Albert"]

surnames = ["Garcia", "Gonzalez", "Rodriguez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Martin",
            "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Munoz", "Alvarez", "Romero", "Alonso", "Gutierrez",
            "Navarro", "Torres", "Dominguez", "Vazquez", "Ramos", "Gil", "Ramirez", "Serrano", "Blanco", "Molina",
            "Morales", "Suarez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marin", "Sanz", "Nunez", "Iglesias",
            "Medina", "Garrido", "Cortes", "Castillo", "Santos", "Lozano", "Guerrero", "Cano", "Prieto", "Mendez",
            "Cruz", "Calvo", "Gallego", "Herrera", "Marquez", "Leon", "Vidal", "Pena", "Flores", "Cabrera", "Campos",
            "Vega", "Fuentes", "Carrasco", "Diez", "Reyes", "Caballero", "Nieto", "Aguilar", "Pascual", "Santana",
            "Herrero", "Montero", "Lorenzo", "Hidalgo", "Gimenez", "Ibanez", "Ferrer", "Duran", "Santiago", "Benitez",
            "Vargas", "Mora", "Vicente", "Arias", "Carmona", "Crespo", "Roman", "Pastor", "Soto", "Saez", "Velasco",
            "Moya", "Soler", "Parra", "Esteban", "Bravo", "Gallardo", "Rojas"]



def get_random_data():
  return get_man_name(),get_surname()

def make_hotdog(mail):
    name, surname = get_random_data()
    dni = dni_maker.generar_dni()
    print("\nMail: " + mail + "\nName: " + name + " \nSurname: " + surname + "\nDNI: " + dni)

    url = "https://www.islas.ikea.es/grancanaria/desktop/es_es/actualizacion/grabarCaptacionConPremio"

    payload = 'campana=QR-SPI-TIENDA&name=' + name + '&last_name_1=' + surname + '' \
              '&email=' + mail + '&genero=1&accept=1'

    headers = {
        'Cookie': "_ga=GA1.2.96618450.1508454967; _ceg.s=oy3fax; _ceg.u=oy3fax; PHPSESSID=ckgi4a5uh8djrs5064tsgnasn2",
        'Origin': "https://www.islas.ikea.es",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "es-ES,es;q=0.9",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'Referer': "https://www.islas.ikea.es/grancanaria/desktop/es_es/micuenta/captacion?^&utm_source=ticket^&utm_medium=qr^&utm_campaign=TICK_SI_ESP^&utm_content=captacion^&utm_term=valoranadido",
        'X-Requested-With': "XMLHttpRequest",
        'Connection': "keep-alive",
        'Cache-Control': "no-cache",
        'Postman-Token': "d0aae5f6-563f-4bae-bdbe-3a7c9e29ab49"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    
    if response.json()['error'] == 0:
        print("    Toc toc, i'm your hotdog!")
    else:
        print("    Error.Maybe you write wrong your email? \n    " + response.json()['texto'])
    time.sleep(0.5)


def get_man_name():
    return man_names[random.randint(0, 99)]

def get_surname():
    return surnames[random.randint(0, 99)]