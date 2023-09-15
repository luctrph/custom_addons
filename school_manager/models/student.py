from odoo import fields, models, api


class Student(models.Model):
    _name = 'student'
    _description = 'Description'

    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    school_id = fields.Many2one(comodel_name="school", string="School")
