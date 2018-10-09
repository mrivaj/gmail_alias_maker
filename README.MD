# Gmail Alias Maker
Utilidad para generar identidades aleatorias, buscando facilitar múltiples registros con una sola dirección de Gmail

[![N|Solid](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.python.org%2Fstatic%2Fcommunity_logos%2Fpython-powered-h-140x182.png&f=1)](https://python.org)
## ¿Cómo funciona?
El script se encarga de generar los diferentes [alias](https://www.labnol.org/internet/multiple-email-addresses-in-gmail/17426/) que admiten las cuentas de Gmail 

Los nombres se generan según los datos del INE (Instituto Nacional de Estadistica), que nos ofrece un listado de los nombres y apellidos más comunes de España. Estos se mezclan aleatoriamente para construir los conjuntos de mail y nombre

El DNI se genera con números aleatorios de 8 cifras y el cálculo del dígito de control correspondiente. Se fuerza que se comience con un 4 porque es la tónica habitual en donde vivo, pero podría eliminarse ese número y aumentar uno el recorrido del bucle

El resultado es un fichero JSON en el que aparecerán las diferentes combinaciones posibles con ese correo, con la siguiente estructura:

```json
[{
"mail": "t.est@gmail.com", 
"name": "Francisco", 
"surname": "Sanz",
"dni":"40923317S"
}]
```

De esta forma, será posible realizar registros múltiples con una sola dirección de Gmail, utilizando herramientas como [Postman Runner](http://blog.getpostman.com/2016/11/22/postmans-new-collection-runner/) para automatizar el proceso

### Notas
  - Gmail permite más alias, ya que se podrían combinar los puntos con las palabras, o añadir más de un punto por correo. No obstante, se quiere mantener algo que pueda ser legible para el usuario, por lo que no se ha implementado
  - Se desarolló una [**versión Java**](https://github.com/mrivaj/gmail-alias-generator), más sencilla (Utiliza ficheros CSV, no JSON), que puede ser de utilidad para futuros desarrollos
  - El módulo de DNI está disponible como Gist [en mi perfil](https://gist.github.com/mrivaj/c892afeff4fb4a988f4951c2dc2253bb)
  - Contacto: [javiersantanagodoy@gmail.com](mailto:javiersantanagodoy@gmail.com)


