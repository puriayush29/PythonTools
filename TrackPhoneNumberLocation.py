import phonenumbers
from phonenumbers import geocoder,carrier

def main():
    phone_number = input("Please enter your phone number with your country code, for example: +88xxxx: ")
    parsed_number = phonenumbers.parse(phone_number,"CH")
    print("The Location: ")
    print(geocoder.description_for_number(parsed_number,"en"))

    ISP_parsed = phonenumbers.parse(phone_number, "RO")
    print(carrier.name_for_valid_number(ISP_parsed, "en"))

if __name__ == '__main__':
    main()