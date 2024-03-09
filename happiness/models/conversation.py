# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HappinessConversation(models.Model):
    _name = "happiness.conversation"
    _description = "Happiness Conversations requests"
    _order = 'create_date desc'

    user_id = fields.Many2one('res.users', string='User')
    user = fields.Char(
        string='Email', related='user_id.email')
    coach_id = fields.Many2one('res.users', string='Conversation with')
    coach = fields.Char(
        string='coach', related='coach_id.email')
    comment = fields.Char('Comments')
    conversation_date = fields.Date(string='Date')
    status = fields.Selection(selection=[('draft', 'Aanvraag'),
                                         ('in_progress', 'Manager toekennen'),
                                         ('done', 'Afgerond')], string='Status', default='draft', group_expand='_read_group_states')

    def _read_group_states(self, values, domain, order):
        selection = self.env['happiness.conversation'].fields_get(allfields=['status'])[
            'status']['selection']
        return [s[0] for s in selection]
