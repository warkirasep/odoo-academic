from odoo import api, fields, models

class Session(models.Model):
    _name = "academic.session"

    name = fields.Char("Name", required=True, size=100)
    course_id = fields.Many2one(comodel_name="academic.course",
        string="Course")

    instructor_id = fields.Many2one(comodel_name="res.partner",
        string="Instuctor")

    start_date = fields.Date("Start Date")

    duration = fields.Integer("Duration")

    seats = fields.Integer("Seats")

    active = fields.Boolean("Is Active", default=True)