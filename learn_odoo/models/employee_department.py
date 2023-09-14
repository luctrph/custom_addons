from odoo import fields, models, api


class EmployeeDepartment(models.Model):
    _name = 'employee.department'
    _description = 'Department Management'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    employee_ids = fields.One2many(
        comodel_name='employee', inverse_name='department_id', string='Employee')
    location = fields.Char(string='Location')
