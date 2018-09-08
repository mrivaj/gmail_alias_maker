generated_alias = []

def make_dot_alias(username,domain):
    for i in range (1,len(username)-1):
        generated_alias.append(username[0:i] + '.' + username[i:len(username)] + '@' + domain)
    generated_alias.append(username[0:len(username)-1] + '.' + username[-1] + '@' + domain)

def print_generated_alias():
    for alias in generated_alias:
        print(alias)

mail = input("Write your gmail account\n")

if mail == "":
    mail = "test@fake.com"

username, domain = mail.split('@')[0], mail.split('@')[1]

print("\nStarting alias creation...\n")
make_dot_alias(username,domain)
print_generated_alias()
