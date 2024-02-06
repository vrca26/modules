from odoo import api, fields, models

class ejemplo02(models.Model):
    _inherit = "eje.01"
    piel = fields.Char(String = "Piel", size = 20, default = "blue")
    paseo = fields.Boolean(String = "Paseo")
    
    is_pretty_name = fields.Boolean(string="is pretty name", compute="_compute_pretty_name")

    date_b = fields.Date("Fecha de adopción", default=fields.Date.today)

    @api.depends("piel","name")
    def _compute_pretty_name(self):
        for record in self:
            record.is_pretty_name = record.piel == "Blue"
    
