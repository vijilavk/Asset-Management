import frappe
@frappe.whitelist()
def get_assigned_asset_count():
    user_email = frappe.db.get_value("User", frappe.session.user, "email")
    employee = frappe.db.get_value("Employee", {"email": user_email})
    if not employee:
        return {"value": 0}
    count = frappe.db.count("Asset", {"assigned_to": employee})
    return {"value": count}
