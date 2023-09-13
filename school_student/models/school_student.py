from odoo import models, api, fields


class schoolstudent(models.Model):
    _name = "school.student"
    _description = 'abc'

    def default_get_rank(self):
        if 1 == 1:
            return 200
        else:
            return 100

    def default_get_date(self):
        return fields.Date.today()

    name = fields.Char(string="School Name", unique=True)
    email = fields.Char(string="Email")
    phone = fields.Char("Phone")
    is_visible = fields.Boolean(string="Is Visible?")
    school_rank = fields.Integer(string="Rank", default=lambda lm: lm.default_get_rank())
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    open_date = fields.Date(default=fields.Date.today())
    school_type = fields.Selection([("private", "Private"), ("public", "Public")]
                                   , default='public')
    document = fields.Binary(string="Document")
    file_name = fields.Char(string="file_name")
    school_image = fields.Image(string="School Image", max_width=100, max_height=100, verify_resolution=False)
    school_description = fields.Html(string="Description")