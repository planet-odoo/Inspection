from odoo import api,fields,models,_

class Fleet_Vehicles(models.Model):
    _inherit = 'fleet.vehicle'

    @api.multi
    def return_action_for_inspection(self):
        """ This opens the xml view specified in xml_id for the current vehicle """
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')
        if xml_id:
            res = self.env['ir.actions.act_window'].for_xml_id('fleet_custom', xml_id)
            res.update(
                context=dict(self.env.context,
                             default_vehicle_id=self.id,
                             license_plate = self.license_plate,
                             model_id = self.model_id.id,
                             brand_id = self.model_id.brand_id.id,
                             year_model = self.model_year,
                             group_by=False),
                domain=[('vehicle_id', '=', self.id)])
            return res
        return False

class AnnualInspection(models.Model):
    _name = 'annual.inspection'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle',required=1)
    annual_digital_signature = fields.Binary('Signature')
    # annual_count = fields.Integer(compute="_compute_count_annual", string="Annual Count")
    owner = fields.Many2one('res.partner','Owner')
    date = fields.Date('Date')
    hour = fields.Float('Time')
    am_pm = fields.Selection([('am','AM'),('pm','PM')])
    address = fields.Text('Address')
    license = fields.Char('License')
    operator = fields.Many2one('res.partner','Operator')
    name = fields.Many2one('res.partner','Name (Inspector/Mechanic/Technician)')
    clapboard = fields.Char('License Plate')
    vin = fields.Char('VIN')
    brand = fields.Many2one('fleet.vehicle.model.brand','Brand')
    model = fields.Many2one('fleet.vehicle.model','Model')
    year = fields.Char('Year')
    #Brakes
    adjustment = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Ajuste')
    drum_disc = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Tambor/Disco')
    sleeves_tubes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Mangas/Tubos')
    bands = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Bandas')
    tractor_prtn_valve = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Válvula Proteccón Tractor')
    compressor = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Compresor')
    service_brakes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Frenos de Servicio')
    parking_brakes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Frenos Estacionamiento')
    electric_brakes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Frenos Eléctricos')
    hydraulic_brakes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Frenos Hidráulicos')
    warning_light = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Luz Advertencia')
    #Guides
    game = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Juego')
    guide_column = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Columna del Guía')
    forward_train = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Tren Delantero')
    guide_box = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Caja del Guía')
    pitman = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Pitman')
    dollies = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Muñequillas/Bolt Joints')
    terminals = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Terminales/Drag Links')
    nuts = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Tuercas')
    liquid = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Líquido "Power Steering"')
    #Windshield(Parabrisas)
    windshield = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Parabrisas')
    #Windshield Wipers(Limpiaparabrisas)
    windshield_wipers = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Limpiaparabrisas')
    #Gas(Combustible)
    leaks = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Filtaciones')
    cover_the_tank = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Tapa el Tanque')
    tank_mount = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Montura del Tanque')
    #Lights(Luces)
    front_directional = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Direccionales delanteras')
    id_clear_front = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'ID/Despejo Delanteras')
    right_marker_light = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Luz Marcadora Derecha')
    left_marker_light = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Luz Marcadora Izquierda')
    rear_directionals = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Direccionales Traseras')
    stop_light = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Luz de Pare "STOP“')
    id_clear_backs = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'ID/Despejo Traseras')
    reflectors = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Reflectores')
    #Coupler(Acoplador)
    fifth_wheel = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Quinta Rueda')
    pintle_hook = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Pintle Hook')
    draw_bar_eye_tounge = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Draw Bar Eye/Tongue')
    chains_cable = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Cadenas/Cables')
    #Exhaust Pipe/Muffler('Tubo Escape/muffler')
    escapes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Escapes')
    proper_installation = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Instalación adecuada')
    #Secure Charging (Carga segura)
    chain = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],'Cadena')

    @api.model
    def default_get(self, fields_list):
        if self._context:
            res = super(AnnualInspection,self).default_get(fields_list)
            res.update({'vehicle_id':self._context.get('default_vehicle_id'),
                        'clapboard':self._context.get('license_plate'),
                        'brand':self._context.get('brand_id'),
                        'model':self._context.get('model_id'),
                        'year':self._context.get('year_model'),
                        })
            return res


class DailyInspection(models.Model):
    _name = 'daily.inspection'

    vehicle_id = fields.Many2one('fleet.vehicle', 'Vehicle', required=True)
    daily_digital_signature = fields.Binary('Signature')
    # daily_count = fields.Integer(compute="_compute_count_daily", string="Daily Count")
    driver = fields.Many2one('res.partner', "Chofer")
    unity = fields.Integer("Unidad")
    clapboard = fields.Char("Tablilla")
    date = fields.Date("Fecha")
    am_time = fields.Float("Hora AM")
    pm_time = fields.Float("Hora PM")
    am_mileage = fields.Float("Millaje AM")
    pm_mileage = fields.Float("Millaje PM")
    #Security Team
    safety_equipment = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Equipo de Seguridad (PPE)")
    fire_extinguisher = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Extintor de Incendios")
    flag = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Bandera")
    reflectors = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Reflectores")
    #Cabin
    safety_belt_and_seats = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Cinturón de Seguridad y Asientos")
    guide_and_management_system = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Guía y Sistema de Dirección")
    rear_view_mirrors = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Espejos Retrovisores")
    horn = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Bocina")
    marbete = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Marbete")
    windshield_and_windshield_wipers = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Parabrisas y Limpia Parabrisas (Wipers)")
    clutch_system_pedal = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Pedal de Sistema de Embrague (Clutch)")
    low_brake_air_pressure_alarm = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Alarma Baja Presión de Aire en Frenos")
    water_temperature = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Temperatura del Agua")
    air_pressure = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Presión de Aire")
    oil_pressure_fuel_other = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Presión de Aceite, Combustible, Otros")
    voltage_indicator = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Indicador de Voltaje")
    interior_cleaning = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Limpieza Interior")
    #Lights
    front_and_rear_lights = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Luces Delanteras y Traseras")
    clapboard_lights = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Luces de Tablilla")
    signals_front_and_rear = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Señales (Delanteras y Traseras)")
    #Exterior and Mechanics
    foot_and_handbrakes = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Frenos de Pie y de Mano")
    rubber_bands_and_rings = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Gomas y Aros")
    water_and_oil_lichens = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Liqueos de Agua y de Aceite")
    strange_noises_in_the_engine = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Ruidos Extraños en el Motor")
    forward_train = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Tren Delantero")
    fuel_tank_and_tank_lid = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Tanque de Combustible y Tapa del Tanque")
    air_pressure_in_the_wheels = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Presión de Aire en las Ruedas")
    oil_and_filter = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Aceite y Filtro")
    brake_hose = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Manguera de Frenos")
    cargo_and_mooring_devices = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Carga y Dispositivos de Amarre")
    fifth_wheel_or_pintle_hook = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Quinta Rueda / Pintle Hook")
    exterior_cleaning = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Limpieza Exterior")
    #Others
    others = fields.Selection([('ok','OK'),('repairer','Reparar'),('na','NA')],"Otros")