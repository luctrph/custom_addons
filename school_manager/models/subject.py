from odoo import fields, models, api


class M_Subject(models.Model):
    _name = 'm.subject'
    _description = 'subject of student'
    name = fields.Char("Name")
    point = fields.Float(string="Point")
    note = fields.Text(string='Note')
    student_id = fields.Many2one(comodel_name="student",string="Student")
