# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school_student(models.Model):
    _name = 'school.student'
    _description = 'school_student.school_student'

    name = fields.Char()
    school_profile_id = fields.Many2one('school.profile', string="School Name", required=True)
    point = fields.Float(string="Point")
    birthday = fields.Date(string='BirthDay')
    address = fields.Text(string='Address')

class SchoolProfile(models.Model):
    _inherit = 'school.profile'

    school_student_ids = fields.One2many(string='Students', comodel_name='school.student',
                                        inverse_name='school_profile_id')