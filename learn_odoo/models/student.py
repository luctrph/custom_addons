from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Student Management'

    name = fields.Char(string="Name")
    dob = fields.Date(string="Birthday")
    address = fields.Text(string="Address")
