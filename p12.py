import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+919491091470")
phone_number2=phonenumbers.parse("+917989848999")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
