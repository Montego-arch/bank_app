import frappe
import requests
import random
from faker import Faker
fake = Faker()
Faker.seed()

def populate_apex():
    #GET MANAGERS
    
    managers = [account_manager.name for account_manager in frappe.db.sql("""SELECT name FROM `tabAccount Manager`;""", as_dict=True)]
    #get  account status
    account_status = ['Savings', 'Domiciliary', 'Current']
    
    #get customer type
    apex_type = [apex_type.name for apex_type in frappe.db.sql("""SELECT name FROM `tabApex Type`;""", as_dict=True)]

    #GET SERVICES
    services = frappe.db.sql("""SELECT service, service_charge FROM `tabApex Financial Service`;""", as_dict=True)

    customer_images = []
    for n in range(5):
        customer_image_url = "https://api.unsplash.com/search/photos?client_id=4FoziFrwX8d0gLNh71fsGq4kdAfd6DzBW6StV9qD0BE&query=african-headshots"
        img_api = requests.get(customer_image_url)
        customer_images += [
                {'doctype': 'Apex',
                #  'services': [services[random.randint(0, len(services)-1)]], 
                 'charges': random.randint(0, 11), 
                 'account_balance': random.randint(40000, 1000000), 
                 'account_number': random.randint(1000003, 2000007),
                 'apex_type': random.choice(apex_type), 
                 'customer_name': fake.profile().get('name'), 
                 'account_status': random.choice(account_status), 
                 'account_manager':random.choice(managers), 
                 'address': fake.address().replace('\n', ', '), 
                 'image': i.get('urls').get('small')} for i in img_api.json().get('results')
                ]
        # print(customer_images)

            #EXECUTE DB CUSTOMER POPULATION
        for p in customer_images:
            # try:
            cs = frappe.get_doc(p) 
            cs.insert(ignore_permissions=True)
            # print("Inserted Customer ", cs.name)
            # except Exception as e:
                # pass
            
        frappe.db.commit()

