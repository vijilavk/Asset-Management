# Asset Manager App

## Overview

- asset_manager is a custom Frappe app for managing assets and assigning them to employees. It includes features like:  
  - Adding and managing assets  
  - Assigning assets to employees  
  - Reporting total assets and asset value
  -Reporting assigned asset for employees
-dash board view for employee asset 

## Installation

1. Get the app from GitHub:  
bench get-app https://github.com/vijilavk/Asset-Management.git

2.Install the app to your site:
bench --site <site_name> install-app asset_manager

3.Apply migrations and build assets:
bench migrate
bench build
bench clear-cache

##Assumptions / Features
Custom DocTypes include:

1.Asset

2.Employee

3.Maintenance Log

4.Maintenance Log Details

-Maintenance Log:

It is a submittable document.

If a Maintenance Log is in Draft, the related Asset's status is Under Maintenance.

If a Maintenance Log is Submitted, the related Asset's status is Available.

-Maintenance Log Details:

It is a child doctype.
