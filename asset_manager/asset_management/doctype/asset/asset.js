// Copyright (c) 2025, vijila and contributors
// For license information, please see license.txt

frappe.ui.form.on("Asset", {
refresh(frm) {
    frm.add_custom_button(('Maintenance Log'),function(){
        frappe.new_doc('Maintenance Log',{
             asset:frm.doc.name
        })
    })
    if(frm.doc.status=="Assigned"){
        frm.add_custom_button(('Retire Asset'),function(){
            frm.set_value("assigned_to",""),
            frm.set_value("status","Retired")
            frm.save()
        })
    }

	},
 });
