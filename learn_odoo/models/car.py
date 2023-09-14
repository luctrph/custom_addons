from odoo import models, fields


class Car(models.Model):
    _name = 'car'
    _description = 'Car Management'
    _rec_name = 'car_type'

    car_type = fields.Char(string='Car Type')
    car_model = fields.Char(string='Car Model')
    manufacturing_year = fields.Integer(string='Manufacturing Year')