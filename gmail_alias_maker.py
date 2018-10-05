import random
import json
import re

generated_alias = []
json_data = []

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
            "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Muñoz", "Alvarez", "Romero", "Alonso", "Gutierrez",
            "Navarro", "Torres", "Dominguez", "Vazquez", "Ramos", "Gil", "Ramirez", "Serrano", "Blanco", "Molina",
            "Morales", "Suarez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marin", "Sanz", "Nuñez", "Iglesias",
            "Medina", "Garrido", "Cortes", "Castillo", "Santos", "Lozano", "Guerrero", "Cano", "Prieto", "Mendez",
            "Cruz", "Calvo", "Gallego", "Herrera", "Marquez", "Leon", "Vidal", "Peña", "Flores", "Cabrera", "Campos",
            "Vega", "Fuentes", "Carrasco", "Diez", "Reyes", "Caballero", "Nieto", "Aguilar", "Pascual", "Santana",
            "Herrero", "Montero", "Lorenzo", "Hidalgo", "Gimenez", "Ibañez", "Ferrer", "Duran", "Santiago", "Benitez",
            "Vargas", "Mora", "Vicente", "Arias", "Carmona", "Crespo", "Roman", "Pastor", "Soto", "Saez", "Velasco",
            "Moya", "Soler", "Parra", "Esteban", "Bravo", "Gallardo", "Rojas"]

words = ["cama","hojas","anteojos","puerta","pantalón","cuchillo","rueda","teclado","librería","estrella","martillo","lentejas","living","zoológico","cinturón","calor","colegio","agua","herramienta","libro","pestaña","piso","tenedor","mensaje","carta","moño","lentes","ensalada","perro","caramelos","guitarra","sol","lapicera","nieve","maletín","granizo","hombre","petróleo","castillo","mono","mano","montañas","explosión","lluvia","ave","taladro","metal","reloj","flor","tornillo"]

def ask_user():
    mail = input("Write your gmail account\n")
    if mail == "":
        mail = "test@fake.com"
    print ("Mail: " + mail)

    mode = input("Choose mode: \n " + 
              "1) Dots \n " +
              "2) Random words \n " +  
              "3) Mixed \n" + 
              "Mode: ")

    return mode, mail.split('@')[0], mail.split('@')[1]

def make_alias(mode,username,domain):
  if mode == "3":
    make_dot_alias(username,domain)
    make_word_alias(username,domain)
  elif mode == "2":
    make_word_alias(username,domain)
  else:
    make_dot_alias(username,domain)

def make_dot_alias(username,domain):
    print("\nCreating dot alias...")

    for i in range (1,len(username)-1):
        generated_alias.append(username[0:i] + '.' + username[i:len(username)] + '@' + domain)
    generated_alias.append(username[0:len(username)-1] + '.' + username[-1] + '@' + domain)
    print("Done!\n")

def make_word_alias(username,domain):
  print("Creating word alias...\n")
  alias_number = int(input("How many alias do you want?"))
  
  if alias_number > 50:
    print("\nMaximum alias number is 50. Reasigned!")
    alias_number = 50

  for i in range (1, alias_number + 1):
    generated_alias.append(username + '+' + get_word() +  '@' + domain)
  
  print ("Done!\n")

def get_man_name():
    return man_names[random.randint(0, 99)]


def get_surnames():
    return surnames[random.randint(0, 99)]

def get_word():
  return words[random.randint(0,49)]


def print_generated_alias():
    for alias in generated_alias:
        json_data.append({
            'mail': alias,
            'name': get_man_name(),
            'surname': get_surnames()
            })
    print ("[" + str(len(generated_alias)) + "] alias created! \n")


def write_json():
    with open('data.json', 'w') as f:
        json.dump(json_data, f, ensure_ascii=False)
    print ("JSON is ready. Bye!\n Use it legally! ;)")


# Use magic
mode, username, domain = ask_user()
make_alias(mode,username,domain)
print_generated_alias()
write_json()
