from odoo import api,fields,models,_

class AnnualInspection(models.Model):
    _name = 'annual.inspection'

    owner = fields.Many2one('res.partner','Owner')
    date = fields.Date('Date')
    hour = fields.Char('Hour')
    address = fields.Text('Address')
    license = fields.Char('License')
    operator = fields.Many2one('res.partner','Operator')
    name = fields.Many2one('res.partner','Name (Inspector/Mechanic/Technician)')
    clapboard = fields.Char('Clapboard')
    vin = fields.Char('VIN')
    brand = fields.Char('Brand')
    model = fields.Char('Model')
    year = fields.Integer('Year')
    #Brakes
    adjustment = fields.Boolean('Ajuste')
    drum_disc = fields.Boolean('Tambor/Disco')
    sleeves_tubes = fields.Boolean('Mangas/Tubos')
    bands = fields.Boolean('Bandas')
    tractor_prtn_valve = fields.Boolean('Válvula Proteccón Tractor')
    compressor = fields.Boolean('Compresor')
    service_brakes = fields.Boolean('Frenos de Servicio')
    parking_brakes = fields.Boolean('Frenos Estacionamiento')
    electric_brakes = fields.Boolean('Frenos Eléctricos')
    hydraulic_brakes = fields.Boolean('Frenos Hidráulicos')
    warning_light = fields.Boolean('Luz Advertencia')
    #Guides




class DailyInspection(models.Model):
    _name = 'daily.inspection'
