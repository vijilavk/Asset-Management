# Copyright (c) 2025, vijila and contributors
# For license information, please see license.txt

import frappe
def execute(filters=None):
	columns = get_columns()
	data= get_data(filters)
	return columns, data
def get_columns():
    return [
        {"label": "ID", "fieldname": "name", "fieldtype": "Link", "options": "Asset", "width": 150},
        {"label": "Asset Name", "fieldname": "asset", "fieldtype": "Data", "width": 150},
        {"label": "Status", "fieldname": "status", "fieldtype": "Select",
         "options": "Available\nAssigned\nUnder Maintenance\nRetired", "width": 150},
        {"label": "Assigned To", "fieldname": "assigned_to", "fieldtype": "Link", "options": "Employee", "width": 150},
        {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 150},
        {"label": "Total Assets", "fieldname": "total_assets", "fieldtype": "Int", "width": 150},
        {"label": "Total Value", "fieldname": "total_value", "fieldtype": "Currency", "width": 150},
		{"label": "Purchase Date", "fieldname": "purchase_date", "fieldtype": "Date", "width": 150},

    ]

def get_data(filters=None):
    data = []
    category_count = {}

    filters = filters or {}
    asset_filters = {}

    if filters.get("category"):
        asset_filters["category"] = filters["category"]

    if filters.get("status"):
        asset_filters["status"] = filters["status"]

    assets = frappe.get_all("Asset", filters=asset_filters, fields=["name","asset_name","status","assigned_to","category","purchase_cost","purchase_date"])

    

    for asset in assets:
        data.append({
            "name": asset.name,
            "asset": asset.asset_name,
            "status": asset.status,
            "assigned_to": asset.assigned_to,
            "category": asset.category,
			"purchase_date":asset.purchase_date,
            "total_assets": 1,  
            "total_value": asset.purchase_cost or 0  
        })

    return data
