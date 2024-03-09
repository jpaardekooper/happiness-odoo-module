# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HappinessResponse(models.Model):
    _name = "happiness.response"
    _description = "Happiness Response overview"
    _order = 'create_date desc'

    user_id = fields.Many2one('res.users', string='Gebruiker')
    work_location = fields.Many2one(
        string='Locatie', related='user_id.department_id')
    note = fields.Char(string='Opmerking')
    happiness = fields.Float(string='Happiness')
    allowed_read = fields.Boolean("Allowed to read", default=True)
