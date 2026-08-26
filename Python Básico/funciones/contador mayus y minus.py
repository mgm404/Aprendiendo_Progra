import re

def count_lower_upper(text):
    uppercase= re.sub('[^A-Z]', '', text) #Pasa x todo el str y quita lo que NO este en mayuscula
    lowercase= re.sub('[^a-z]', '', text) #Pasa x todo el str y quita lo que NO este en minuscula
    uppercase_count=len(uppercase) #Cuenta la cantidad de letras mayus
    lowercase_count=len(lowercase) #Cuenta la cantidad de letras minus
    print(f"La cantidad de mayusculas es: {uppercase_count}, y minúsculas es de: {lowercase_count}")


super_text="Hola Mundo, huevo con pan"
print(super_text)
count_lower_upper(super_text)
