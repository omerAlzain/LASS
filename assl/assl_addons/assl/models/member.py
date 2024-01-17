from odoo import models, fields, api

class AsslMember(models.Model):
    _name = 'assl.member'
    _description = "Membre d\'assl"

    name = fields.Char(string='Nom, Prénom', required=True)
    date_adhesion = fields.Date(string='Date d\'adhésion', default=fields.Date.today())
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Téléphone')
    genre = fields.Selection([('homme', 'Homme'), ('femme', 'Femme'), ('autre', 'Autre')], string='Genre')



