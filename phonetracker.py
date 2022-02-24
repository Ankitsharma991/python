import phonenumbers 
from test import Number
from phonenumber import geocoder 
ch_nmbr = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_nmber,"en"))
