import datetime
class person:
    def __init__(self,name,surname,birthdate,address,Mobile_no,email):
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.address=address
        self.Mobile_no=Mobile_no
        self.email=email
    def age(self):
        today=datetime.date.today()
        age=today.year - self.birthdate.year
        if today < datetime.date(today.year,self.birthdate.month,self.birthdate.day):
            age-=1
        return age
person=person("Vishal","Sharma",datetime.date(2004,10,15),"Virar,Bombay 401305","9420456789","mrsharmajireal@gmail.com")
print(person.name)
print(person.surname)
print(person.email)
print(person.age())
print(person.address)
print(person.Mobile_no)
