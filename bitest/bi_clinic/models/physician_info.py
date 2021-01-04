from odoo import fields, models, api

class PatientMedicament(models.Model):
    _name = 'bi.physician.info'
    _description = 'bi_clinic.physician.info'
    _rec_name = 'physician_id'

    physician_id = fields.Many2one('res.partner', string="Physician Name", domain="[('is_doctor','=',True)]")
    speciality_id = fields.Many2one('bi.speciality',string="Speciality")
    physician_no = fields.Char(string="ID")
    institution_id = fields.Many2one('bi.institution',string="Institution")

    @api.model
    def create(self, vals):
        newid = super(PatientMedicament, self).create(vals)
        record_to_update = self.env['res.partner'].browse(vals.get('physician_id'))
        record_to_update.write({'is_doctor':True})
        return newid
        