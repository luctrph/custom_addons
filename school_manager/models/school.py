from odoo import fields, models, api


class School(models.Model):
    _name = 'school'
    _description = 'School'

    name = fields.Char(string='Name')
    address = fields.Text(string='Address')
    student_ids = fields.One2many(comodel_name="student", inverse_name="school_id", string="Student")
