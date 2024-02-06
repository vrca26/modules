from odoo import api, fields, models
#Probando 1
class ejemplo01(models.Model):
    _name = "eje.01"
    name  = fields.Char(string = "name", required = True)
    age = fields.Integer(String = "age", required = True)
    color = fields.Char(String = "color", required = True)
    is_new = fields.Boolean(String ="is_new", required = True)
    type = fields.Selection([
        ("dog","Dog"),
        ("cat","Cat"),
        ("bird","Bird"),
        ("fish","Fish"),
        ("other","Other")],String ="type", default = "small", required = True)
