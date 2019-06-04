# -*- coding: utf-8 -*-

{
    "name": "Inspection in Fleet",
    "version": "10.0",
    "category": "Fleet",
    "author": "Planet-Odoo",
    "website": "http://www.planet-odoo.com",
    "depends": ["base", "fleet","web",],
    "data": [
        'data.xml',
        'security/ir.model.access.csv',
        'views/inspection.xml',
        'views/annual_inspection.xml',
        'views/daily_inspection.xml',
        'reports/inspection_reports.xml',
        'reports/inspection_templates.xml',
    ],
    "qweb": [],
    "installable": True,
    "auto_install": False,
}
