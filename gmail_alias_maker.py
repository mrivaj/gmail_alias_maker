import random
import json
import re

generated_alias = []
json_data = []


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
  alias_number = int(input("How many word alias do you want?\n"))
  
  if alias_number > 50:
    print("\nMaximum alias number is 50. Reasigned!")
    alias_number = 50

  for i in range (1, alias_number + 1):
    generated_alias.append(username + '+' + get_word() +  '@' + domain)
  
  print ("Done!\n")


def get_word():
  return words[random.randint(0,49)]


def get_generated_alias():
  return generated_alias

def get_mail():
  return username + '@' + domain

# Use magic
print("#####   Hotdog Maker   #####\n")
mode, username, domain = ask_user()
make_alias(mode,username,domain)
get_generated_alias()
