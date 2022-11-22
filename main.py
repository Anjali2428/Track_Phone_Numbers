import phonenumbers

from test import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_number, "hi")
print(location)

from phonenumbers import carrier
service_name = phonenumbers.parse(number)
print(carrier.name_for_number(service_name, 'en'))


