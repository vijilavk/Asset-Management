# Copyright (c) 2025, vijila and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class MaintenanceLog(Document):

    def on_submit(self):
        asset = frappe.get_doc("Asset", self.asset)
        if asset:
            asset.append('maintenance_logs', {
                "maintenance_log_id": self.name,
                "date": self.date,
                "cost": self.cost,
                "description": self.description
            })
            asset.save()
            frappe.msgprint("Asset maintenance details added to maintenance log details table")

    def validate(self):
        if self.asset:
            asset_exists = frappe.db.exists("Asset", self.asset)
            if asset_exists:
                asset = frappe.get_doc("Asset", self.asset)
                if self.docstatus == 0:
                    asset.status = "Under Maintenance"
                elif self.docstatus == 1:
                    asset.status = "Available"
                asset.save()
