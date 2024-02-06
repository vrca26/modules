from odoo import api, fields, models

class ejemplo02(models.Model):
    _inherit = "eje.01"
    piel = fields.Char(String = "Piel", size = 20, default = "blue")
    paseo = fields.Boolean(String = "Paseo")
    