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
    driver_signature = fields.Binary('Driver Signature')
    inspector_signature = fields.Binary('Inspector Signature')
    driver = fields.Many2one('res.partner', "Chofer")
    unity = fields.Integer("Unidad")
    clapboard = fields.Char("Tablilla")
    date = fields.Date("Fecha")
    am_time = fields.Float("Hora AM")
    pm_time = fields.Float("Hora PM")
    am_mileage = fields.Float("Millaje AM")
    pm_mileage = fields.Float("Millaje PM")
    #Security Team
    safety_equipment_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Equipo de Seguridad (PPE)")
    safety_equipment_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Equipo de Seguridad (PPE)")
    safety_equipment_bt_comm = fields.Char('Comment')
    safety_equipment_at_comm = fields.Char('Comment')
    fire_extinguisher_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Extintor de Incendios")
    fire_extinguisher_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Extintor de Incendios")
    fire_extinguisher_bt_comm = fields.Char('Comment')
    fire_extinguisher_at_comm = fields.Char('Comment')
    flag_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Bandera")
    flag_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Bandera")
    flag_bt_comm = fields.Char('Comment')
    flag_at_comm = fields.Char('Comment')
    reflectors_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Reflectores")
    reflectors_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Reflectores")
    reflectors_bt_comm = fields.Char('Comment')
    reflectors_at_comm = fields.Char('Comment')
    #Cabin
    safety_belt_and_seats_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Cinturón de Seguridad y Asientos")
    safety_belt_and_seats_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Cinturón de Seguridad y Asientos")
    safety_belt_and_seats_bt_comm = fields.Char('Comment')
    safety_belt_and_seats_at_comm = fields.Char('Comment')

    guide_and_management_system_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Guía y Sistema de Dirección")
    guide_and_management_system_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Guía y Sistema de Dirección")
    guide_and_management_system_bt_comm = fields.Char('Comment')
    guide_and_management_system_at_comm = fields.Char('Comment')

    rear_view_mirrors_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Espejos Retrovisores")
    rear_view_mirrors_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Espejos Retrovisores")
    rear_view_mirrors_bt_comm = fields.Char('Comment')
    rear_view_mirrors_at_comm = fields.Char('Comment')

    horn_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Bocina")
    horn_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Bocina")
    horn_bt_comm = fields.Char('Comment')
    horn_at_comm = fields.Char('Comment')

    marbete_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Marbete")
    marbete_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Marbete")
    marbete_bt_comm = fields.Char('Comment')
    marbete_at_comm = fields.Char('Comment')

    windshield_and_windshield_wipers_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Parabrisas y Limpia Parabrisas (Wipers)")
    windshield_and_windshield_wipers_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Parabrisas y Limpia Parabrisas (Wipers)")
    windshield_and_windshield_wipers_bt_comm = fields.Char('Comment')
    windshield_and_windshield_wipers_at_comm = fields.Char('Comment')

    clutch_system_pedal_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Pedal de Sistema de Embrague (Clutch)")
    clutch_system_pedal_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Pedal de Sistema de Embrague (Clutch)")
    clutch_system_pedal_bt_comm = fields.Char('Comment')
    clutch_system_pedal_at_comm = fields.Char('Comment')

    low_brake_air_pressure_alarm_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Alarma Baja Presión de Aire en Frenos")
    low_brake_air_pressure_alarm_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Alarma Baja Presión de Aire en Frenos")
    low_brake_air_pressure_alarm_bt_comm = fields.Char('Comment')
    low_brake_air_pressure_alarm_at_comm = fields.Char('Comment')

    water_temperature_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Temperatura del Agua")
    water_temperature_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Temperatura del Agua")
    water_temperature_bt_comm = fields.Char('Comment')
    water_temperature_at_comm = fields.Char('Comment')

    air_pressure_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Presión de Aire")
    air_pressure_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Presión de Aire")
    air_pressure_bt_comm = fields.Char('Comment')
    air_pressure_at_comm = fields.Char('Comment')

    oil_pressure_fuel_other_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Presión de Aceite, Combustible, Otros")
    oil_pressure_fuel_other_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Presión de Aceite, Combustible, Otros")
    oil_pressure_fuel_other_bt_comm = fields.Char('Comment')
    oil_pressure_fuel_other_at_comm = fields.Char('Comment')

    voltage_indicator_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Indicador de Voltaje")
    voltage_indicator_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Indicador de Voltaje")
    voltage_indicator_bt_comm = fields.Char('Comment')
    voltage_indicator_at_comm = fields.Char('Comment')

    interior_cleaning_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Limpieza Interior")
    interior_cleaning_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Limpieza Interior")
    interior_cleaning_bt_comm = fields.Char('Comment')
    interior_cleaning_at_comm = fields.Char('Comment')

    #Lights
    front_and_rear_lights_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Luces Delanteras y Traseras")
    front_and_rear_lights_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Luces Delanteras y Traseras")
    front_and_rear_lights_bt_comm = fields.Char('Comment')
    front_and_rear_lights_at_comm = fields.Char('Comment')

    clapboard_lights_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Luces de Tablilla")
    clapboard_lights_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Luces de Tablilla")
    clapboard_lights_bt_comm = fields.Char('Comment')
    clapboard_lights_at_comm = fields.Char('Comment')

    signals_front_and_rear_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Señales (Delanteras y Traseras)")
    signals_front_and_rear_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Señales (Delanteras y Traseras)")
    signals_front_and_rear_bt_comm = fields.Char('Comment')
    signals_front_and_rear_at_comm = fields.Char('Comment')

    #Exterior and Mechanics

    foot_and_handbrakes_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Frenos de Pie y de Mano")
    foot_and_handbrakes_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Frenos de Pie y de Mano")
    foot_and_handbrakes_bt_comm = fields.Char('Comment')
    foot_and_handbrakes_at_comm = fields.Char('Comment')

    rubber_bands_and_rings_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Gomas y Aros")
    rubber_bands_and_rings_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Gomas y Aros")
    rubber_bands_and_rings_bt_comm = fields.Char('Comment')
    rubber_bands_and_rings_at_comm = fields.Char('Comment')

    water_and_oil_lichens_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Liqueos de Agua y de Aceite")
    water_and_oil_lichens_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Liqueos de Agua y de Aceite")
    water_and_oil_lichens_bt_comm = fields.Char('Comment')
    water_and_oil_lichens_at_comm = fields.Char('Comment')

    strange_noises_in_the_engine_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Ruidos Extraños en el Motor")
    strange_noises_in_the_engine_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Ruidos Extraños en el Motor")
    strange_noises_in_the_engine_bt_comm = fields.Char('Comment')
    strange_noises_in_the_engine_at_comm = fields.Char('Comment')

    forward_train_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Tren Delantero")
    forward_train_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Tren Delantero")
    forward_train_bt_comm = fields.Char('Comment')
    forward_train_at_comm = fields.Char('Comment')

    fuel_tank_and_tank_lid_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Tanque de Combustible y Tapa del Tanque")
    fuel_tank_and_tank_lid_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Tanque de Combustible y Tapa del Tanque")
    fuel_tank_and_tank_lid_bt_comm = fields.Char('Comment')
    fuel_tank_and_tank_lid_at_comm = fields.Char('Comment')

    air_pressure_in_the_wheels_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Presión de Aire en las Ruedas")
    air_pressure_in_the_wheels_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Presión de Aire en las Ruedas")
    air_pressure_in_the_wheels_bt_comm = fields.Char('Comment')
    air_pressure_in_the_wheels_at_comm = fields.Char('Comment')

    oil_and_filter_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Aceite y Filtro")
    oil_and_filter_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Aceite y Filtro")
    oil_and_filter_bt_comm = fields.Char('Comment')
    oil_and_filter_at_comm = fields.Char('Comment')

    brake_hose_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Manguera de Frenos")
    brake_hose_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Manguera de Frenos")
    brake_hose_bt_comm = fields.Char('Comment')
    brake_hose_at_comm = fields.Char('Comment')

    cargo_and_mooring_devices_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Carga y Dispositivos de Amarre")
    cargo_and_mooring_devices_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Carga y Dispositivos de Amarre")
    cargo_and_mooring_devices_bt_comm = fields.Char('Comment')
    cargo_and_mooring_devices_at_comm = fields.Char('Comment')

    fifth_wheel_or_pintle_hook_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Quinta Rueda / Pintle Hook")
    fifth_wheel_or_pintle_hook_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Quinta Rueda / Pintle Hook")
    fifth_wheel_or_pintle_hook_bt_comm = fields.Char('Comment')
    fifth_wheel_or_pintle_hook_at_comm = fields.Char('Comment')

    exterior_cleaning_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Limpieza Exterior")
    exterior_cleaning_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Limpieza Exterior")
    exterior_cleaning_bt_comm = fields.Char('Comment')
    exterior_cleaning_at_comm = fields.Char('Comment')

    #Others
    others_bt = fields.Selection([('ok','OK'),('damaged','Dañado')],"Otros")
    others_at = fields.Selection([('ok','OK'),('damaged','Dañado')],"Otros")
    others_bt_comm = fields.Char('Comment')
    others_at_comm = fields.Char('Comment')

    # @api.model
    # def default_get(self, fields_list):
    #     if self._context:
    #         res = super(DailyInspection, self).default_get(fields_list)
    #         res.update({'vehicle_id': self._context.get('default_vehicle_id'),
    #                     'clapboard': self._context.get('license_plate'),
    #                     'brand': self._context.get('brand_id'),
    #                     'model': self._context.get('model_id'),
    #                     'year': self._context.get('year_model'),
    #                     })
    #         return res