import json
import random

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

def main():
    username, domain = ask_user()
    make_dot_alias(username, domain)
    print_generated_alias()

def ask_user():
    mail = input("Write your gmail account\n")

    if mail == "":
        mail = "test@fake.com"
    print ("Mail: " + mail)
    return mail.split('@')[0], mail.split('@')[1]


def make_dot_alias(username,domain):
    print("\nStarting alias creation...\n")

    for i in range (1,len(username)-1):
        generated_alias.append(username[0:i] + '.' + username[i:len(username)] + '@' + domain)
    generated_alias.append(username[0:len(username)-1] + '.' + username[-1] + '@' + domain)

def get_man_name():
    return man_names[random.randint(0, 99)]

def get_surnames():
    return surnames[random.randint(0, 99)]

def print_generated_alias():
    for alias in generated_alias:
        json_data.append({
            'mail': alias,
            'name': get_man_name(),
            'surname': get_surnames()
            })
    print("Alias created.")

main()


