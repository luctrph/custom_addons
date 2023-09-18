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
    hoddy_list = fields.Many2many(comodel_name='hobby',relation='school_hoddy_rel',column1='student_id',column2='hoddy_id',string='Hoddies')
    school_type = fields.Selection([("private", "Private"), ("public", "Public")],string='School type',related='school_profile_id.school_type')
    school_visiable = fields.Boolean(related='school_profile_id.is_visible', string='School visiable',store=True)


class SchoolProfile(models.Model):
    _inherit = 'school.profile'

    school_student_ids = fields.One2many(string='Students', comodel_name='school.student',
                                        inverse_name='school_profile_id')



class Hobbies(models.Model):
    _name = "hobby"
    _description = "hobby of student"
    name = fields.Char("Hobby")
