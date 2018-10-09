#!/usr/bin/python
import hotdog_maker as food
import gmail_alias_maker as alias


## DEBERIA SER MAIL LIST
mail_list = alias.get_generated_alias()
print("Alias created: " + str(len(mail_list)))
print("m4k3_1t_r41n...\n")
for mail in mail_list:
  food.make_hotdog(mail)
print("\nAll done! Enjoy\n")