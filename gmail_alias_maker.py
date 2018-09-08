generated_alias = []

def make_dot_alias(username,domain):
    for i in range (1,len(username)-1):
        generated_alias.append(username[0:i] + '.' + username[i:len(username)] + '@' + domain)
    generated_alias.append(username[0:len(username)-1] + '.' + username[-1] + '@' + domain)
    print("Alias generated: " + str(len(generated_alias)))
    
mail = "yourmail@javi.com"

username, domain = mail.split('@')[0], mail.split('@')[1]

make_dot_alias(username,domain)
