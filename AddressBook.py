class BaseContact:
    def __init__(self, name, surname, email_address,phone_number):
        self.name = name
        self.surname = surname
        self.email_address = email_address
        self.phone_number = phone_number

    def personal_information(self):
        print(f"Wybieram numer prywatny: {self.phone_number}, i dzwonię do: {self.name} {self.surname}")


    def __str__(self):
        return f"{self.name} {self.surname}, Email: {self.email_address}"
    
    @property
    def label_length(self):
        return len(f"{self.name} {self.surname}")
    
class BusinessContact(BaseContact):
    def __init__(self, name, surname, email_address, position, company, work_phone, phone_number):
        super().__init__(name, surname, email_address,phone_number)
        self.position = position
        self.company = company
        self.work_phone = work_phone
    
    def contact(self):
        print(f"Wybieram numer słuzbowy: {self.work_phone}, i dzwonię do: {self.name} {self.surname}")


kowalczyk = BusinessContact(name="Michał", surname="Kowalczyk", email_address="michalkow@gmail.com", 
                            position="IT Engineer", company="Google", work_phone="+48600500300",phone_number="+48222333555")
duda = BusinessContact(name="Justyna", surname="Duda", email_address="justina.duda@gmail.com", 
                       position="Senior Accountant", company="UBS", work_phone="+48505456789",phone_number="+48123456789")
rymar = BusinessContact(name="Marta", surname="Rymar", email_address="martarymar@gmail.com", 
                        position="Administration Employee", company="HSBC", work_phone="+48222354678",phone_number="+48967854234")
dąbroś=BusinessContact(name="Anna",surname="Dąbroś",email_address="annadabros@gmail.com",
                   position="Finansial Analyst",company="ABB",work_phone="+48608934567",phone_number="+48345789006")
figiela=BusinessContact(name="Aneta",surname="Figiela",email_address="anetafigile@gmail.com",
                    position="Java Developer",company="Comarch",work_phone="+48456785345",phone_number="+48567000333")

contacts = [kowalczyk, duda, rymar,dąbroś,figiela]


for contact in contacts:
 contact.contact()   
 print(f"{contact.name} {contact.surname}: {contact.label_length} znaków")
 contact.personal_information()
 
from faker import Faker

fake=Faker()

def create_contacts(contact_type, quantity):
    for _ in range(quantity):
        print(f"\n{'Prywatna wizytówka:' if contact_type == 'base' else 'Biznesowa wizytówka:'}")
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        
        print(f"Imię i nazwisko: {name}")
        print(f"Email: {email}")
        print(f"Telefon: {phone_number}")
        
        if contact_type == 'business':
            position = fake.job()
            company = fake.company()
            print(f"Stanowisko: {position}")
            print(f"Firma: {company}")


create_contacts("base", 3)
create_contacts("business", 2)
