from pydantic import BaseModel, field_validator


#creation de la class baseModel
class User(BaseModel):
    name:str
    Surname:str
    email:str
    account_id:int

#creation d'un exemple de la model
user=User(
    name="salah",
    Surname="salah",
    email="salah@gmail.com",
    account_id = 12345)
#Affichage de donneé

print(user.name)
print(user.email)
print(user.account_id)

#creation d'un autre exemple avec unpacking a dictionary
user_data={
    'name':'sirine',
    'Surname':'chebbi',
    'email':'chebbisirine59@gmail.com',
    'account_id':97322
}
user2=User(**user_data)
#Affichage du donnée du 2 eme user
print(" ")
print(user2)

@field_validator("account_id")
def validate_account_id(cls,value):
    if value <= 0:
        raise ValueError(f"account_id must be positive : {value}")
    return value
#Un ERREUR va survenu apres exection de cet exemple
# car account_id < 0
#user = User(name = 'Asma', email = 'Asma', account_id = -12)
#print(user)

#Affichage en JSON string
user_json_str=user2.model_dump_json()
print(user_json_str)
#Affichage  en Objet
user_json_obj = user.model_dump()
print(user_json_obj)


