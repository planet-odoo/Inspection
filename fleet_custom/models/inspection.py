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
    game = fields.Boolean('Juego')
    guide_column = fields.Boolean('Columna del Guía')
    forward_train = fields.Boolean('Tren Delantero')
    guide_box = fields.Boolean('Caja del Guía')
    pitman = fields.Boolean('Pitman')
    dollies = fields.Boolean('Muñequillas/Bolt Joints')
    terminals = fields.Boolean('Terminales/Drag Links')
    nuts = fields.Boolean('Tuercas')
    liquid = fields.Boolean('Líquido "Power Steering"')
    #Windshield(Parabrisas)
    #Windshield Wipers(Limpiaparabrisas)
    #Gas(Combustible)
    leaks = fields.Boolean('Filtaciones')
    cover_the_tank = fields.Boolean('Tapa el Tanque')
    tank_mount = fields.Boolean('Montura del Tanque')
    #Lights(Luces)
    front_directional = fields.Boolean('Direccionales delanteras')
    id_clear_front = fields.Boolean('ID/Despejo Delanteras')
    right_marker_light = fields.Boolean('Luz Marcadora Derecha')
    left_marker_light = fields.Boolean('Luz Marcadora Izquierda')
    rear_directionals = fields.Boolean('Direccionales Traseras')
    stop_light = fields.Boolean('Luz de Pare "STOP“')
    id_clear_backs = fields.Boolean('ID/Despejo Traseras')
    reflectors = fields.Boolean('Reflectores')
    #Coupler(Acoplador)
    fifth_wheel = fields.Boolean('Quinta Rueda')
    pintle_hook = fields.Boolean('Pintle Hook')
    draw_bar_eye_tounge = fields.Boolean('Draw Bar Eye/Tongue')
    chains_cable = fields.Boolean('Cadenas/Cables')
    #Exhaust Pipe/Muffler('Tubo Escape/muffler')
    escapes = fields.Boolean('Escapes')
    proper_installation = fields.Boolean('Instalación adecuada')
    #Secure Charging (Carga segura)
    chain = fields.Boolean('Cadena')



class DailyInspection(models.Model):

    _name = 'daily.inspection'

    driver = fields.Many2one('res.partner', "Chofer")
    unity = fields.Integer("Unidad")
    clapboard = fields.Char("Tablilla")
    date = fields.Date("Fecha")
    am_time = fields.Float("Hora AM")
    pm_time = fields.Float("Hora PM")
    am_mileage = fields.Float("Millaje AM")
    pm_mileage = fields.Float("Millaje PM")

    #Security Team

    safety_equipment = fields.Boolean("Equipo de Seguridad (PPE)")
    fire_extinguisher = fields.Boolean("Extintor de Incendios")
    flag = fields.Boolean("Bandera")
    reflectors = fields.Boolean("Reflectores")

    #Cabin

    safety_belt_and_seats = fields.Boolean("Cinturón de Seguridad y Asientos")
    guide_and_management_system = fields.Boolean("Guía y Sistema de Dirección")
    rear_view_mirrors = fields.Boolean("Espejos Retrovisores")
    horn = fields.Boolean("Bocina")
    marbete = fields.Boolean("Marbete")
    windshield_and_windshield_wipers = fields.Boolean("Parabrisas y Limpia Parabrisas (Wipers)")
    clutch_system_pedal = fields.Boolean("Pedal de Sistema de Embrague (Clutch)")
    low_brake_air_pressure_alarm = fields.Boolean("Alarma Baja Presión de Aire en Frenos")
    water_temperature = fields.Boolean("Temperatura del Agua")
    air_pressure = fields.Boolean("Presión de Aire")
    oil_pressure_fuel_other = fields.Boolean("Presión de Aceite, Combustible, Otros")
    voltage_indicator = fields.Boolean("Indicador de Voltaje")
    interior_cleaning = fields.Boolean("Limpieza Interior")

    #Lights

    front_and_rear_lights = fields.Boolean("Luces Delanteras y Traseras")
    clapboard_lights = fields.Boolean("Luces de Tablilla")
    signals_front_and_rear = fields.Boolean("Señales (Delanteras y Traseras)")

    #Exterior and Mechanics

    foot_and_handbrakes = fields.Boolean("Frenos de Pie y de Mano")
    rubber_bands_and_rings = fields.Boolean("Gomas y Aros")
    water_and_oil_lichens = fields.Boolean("Liqueos de Agua y de Aceite")
    strange_noises_in_the_engine = fields.Boolean("Ruidos Extraños en el Motor")
    forward_train = fields.Boolean("Tren Delantero")
    fuel_tank_and_tank_lid = fields.Boolean("Tanque de Combustible y Tapa del Tanque")
    air_pressure_in_the_wheels = fields.Boolean("Presión de Aire en las Ruedas")
    oil_and_filter = fields.Boolean("Aceite y Filtro")
    brake_hose = fields.Boolean("Manguera de Frenos")
    cargo_and_mooring_devices = fields.Boolean("Carga y Dispositivos de Amarre")
    fifth_wheel_or_pintle_hook = fields.Boolean("Quinta Rueda / Pintle Hook")
    exterior_cleaning = fields.Boolean("Limpieza Exterior")

    #Others

    others = fields.Boolean("Otros")