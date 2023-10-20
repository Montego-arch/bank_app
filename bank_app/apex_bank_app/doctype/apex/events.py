import frappe
from bank_app.utils import sendmail


def validate(doc, event):
    pass
    # print(f"\n\n\n\n{doc}, {event}")
    # frappe.throw("Error Occured")

def on_update(doc, event):
    print(f"\n\n\n\n{doc}, {event}")
    frappe.msgprint(f"{doc.name} has been updated by {doc.owner}")

def after_insert(doc, event):
    # create note after an account is created
    note = frappe.get_doc({
        'doctype':'Note',
        'title': f"{doc.name} Added",
        'public': True,
        'content': doc.account_status
    })
    note.insert()
    frappe.db.commit()
    frappe.msgprint(f"{note.title} has been created.")
    # send mail
    # doc, recipients, msg, title, attachments=None)
    account_manager_email = frappe.get_doc('Account Manager', doc.account_manager)
    msg = f"Hello <b>{doc.manager_name}, an account has been opened by you.</b>"
    attachments = [frappe.attach_print(doc.doctype, doc.name, file_name=doc.name),]
    sendmail(doc, [account_manager_email, 'ross@mail.com'],msg, 'New Account', attachments)