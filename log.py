from odoo import models, fields

class log(models.Model):
  _name = "log.log"

  partner = fields.Many2one('res.partner', 'Partner')
  nombre_archivo = fields.Char('Nombre de Archivo')
  create_date = fields.Datetime('Fecha', readonly=True)
