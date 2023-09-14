from odoo import fields, models, api


class Employee(models.Model):
    _name = 'employee'
    _description = 'Employee Manager'

    name = fields.Char(string='Name')
    gender = fields.Selection(
        string='Gender', selection=[('male', 'Male'), ('female', 'Female')])
    married = fields.Boolean(string='Married?', default=False)
    state = fields.Selection(
        selection=[('onboard', 'On Board'), ('leave', 'Leave')],
        string='State', default='onboard')
    department_id = fields.Many2one(
        comodel_name='employee.department', string='Department')
