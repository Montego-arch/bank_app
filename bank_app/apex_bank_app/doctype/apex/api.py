import frappe

@frappe.whitelist()
def check_account_types(apex_type):
    return frappe.db.sql(f"""SELECT name, apex_type FROM `tabApex` WHERE apex_type='{apex_type}';""", as_dict=True)

