from odoo import api,fields,models,_

class Mail_Activity(models.Model):
    _inherit = 'mail.activity'

    @api.model
    def create(self,values):
        lst = ['annual.inspection','daily.inspection']
        vals = values
        inspection_activity = super(Mail_Activity,self).create(values)
        if inspection_activity.res_model in lst:
            res_id = self.env[inspection_activity.res_model].search([('id','=',inspection_activity.res_id)])
            vals['res_model_id'] = self.env['ir.model']._get('fleet.vehicle').id
            vals.update({'res_id':res_id.vehicle_id.id,
                        'res_model':'fleet.vehicle',})
            vehicle_activity = super(Mail_Activity,self).create(vals)
        return inspection_activity

