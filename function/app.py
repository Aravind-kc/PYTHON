name = "kc"
ph = "98989898"
email = "kc.wizaravind@gmail.com"

#def insert_to_db(name, ph, email, gender = "NA", address = "m"):

    # insert Db Query
 #   print(name, ph, email, gender, address)

#insert_to_db(ph, name, email)

def string_to_dict(name, ph, email):
    c= {
        "key1" : name,
        "key2" : ph,
        "key3" : email,
    }
    return c
def print_function():
    key1 = string_to_dict(ph="1111", name="kc", email="email1")
    key2 = string_to_dict(ph="2222", name="rs", email="email2")
    key3 = string_to_dict(ph="3333", name="ed", email="email3")
    list_of_dict= [key1, key2, key3]
    print(list_of_dict)

    print_function()
