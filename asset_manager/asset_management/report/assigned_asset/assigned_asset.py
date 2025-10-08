import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data()
    return columns, data


def get_columns():
    return [
        {"label": "Asset ID", "fieldname": "name", "fieldtype": "Link", "options": "Asset", "width": 150},
        {"label": "Asset Name", "fieldname": "asset_name", "fieldtype": "Data", "width": 200},
        {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 150},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": "Purchase Date", "fieldname": "purchase_date", "fieldtype": "Date", "width": 120},
        {"label": "Purchase Cost", "fieldname": "purchase_cost", "fieldtype": "Currency", "width": 120},
    ]


def get_data():
    user_email = frappe.db.get_value("User", frappe.session.user, "email")
    print("User Email:", user_email)

    if not user_email:
        frappe.msgprint("No email found for this user.")
        return []

    employee = frappe.db.get_value("Employee", {"email": user_email}, "name")
    print("Employee:", employee)

    if not employee:
        frappe.msgprint("No Employee record found for this email.")
        return []

    assets = frappe.get_all(
        "Asset",
        filters={"assigned_to": employee},
        fields=["name", "asset_name", "category", "status", "purchase_date", "purchase_cost"],
        order_by="purchase_date desc"
    )

    data = []
    for asset in assets:
        data.append({
            "name": asset.name,
            "asset_name": asset.asset_name,
            "category": asset.category,
            "status": asset.status,
            "purchase_date": asset.purchase_date,
            "purchase_cost": asset.purchase_cost,
        })

    return data

