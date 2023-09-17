from odoo import models, fields, api, _
import base64
import socket


class StudentFeedback(models.Model):
    _name = 'student.feedback'
    _description = 'Student Feedback'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'student_name'

    student_name = fields.Char('Student Name', readonly=True)
    coordinator_id = fields.Many2one('res.users', string='Coordinator', readonly=True)
    batch_id = fields.Many2one('logic.base.batch', string='Batch', readonly=True)
    star_rating = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        readonly=True
    )
    feedback = fields.Text('Feedback', readonly=True)
    rating = fields.Float()
    text_to_copy = fields.Char(string='Text to Copy')
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)

    def current_url_link_feedback(self):
        current_user = self.env['res.users'].browse(self._uid).id

        print(current_user, 'user')
        int_bytes = current_user.to_bytes((current_user.bit_length() + 7) // 8, 'big')
        base64_string = base64.b64encode(int_bytes).decode('utf-8')
        print(base64_string, 'base64')

        company = self.env['res.company'].search([('id', '=', self.env.company.id)])
        print(company.website, 'wwewwwwww')
        print(company, 'fjksdhg')
        print('https://corp.logiceducation.org/feedback/' + str(current_user), 'url')
        self.text_to_copy = 'https://corp.logiceducation.org/feedback/' + base64_string
        print(self.text_to_copy, 'url_cop')
        return {'name': _('Feedback Link'),
                'type': 'ir.actions.act_window',
                'res_model': 'copy.link.wizard.feedback',
                'view_mode': 'form',
                'target': 'new',
                'context': {'default_link': company.website+ '/feedback/' + base64_string},
                }

    # def current_url_link_feedback_url(self):
    #     base_url = self.env['ir.config_parameter'].get_param('web.base.url')
    #     current_url = self.env.context.get('web.base.url', '') + '/web#id=%s&view_type=form&model=%s' % (
    #         self.id, self._name)
    #     print(current_url, 'url')
    #     current_user = self.env['res.users'].browse(self._uid).id
    #
    #     print(current_user, 'user')
    #     print('https://corp.logiceducation.org/feedback/' + str(current_user), 'url')
    #     self.text_to_copy = 'https://corp.logiceducation.org/feedback/' + str(current_user)
        # return {
        #     'name': 'Current URL',
        #     'type': 'ir.actions.act_url',
        #     'target': 'new',
        #     'url': current_url,
        # }


class CopyLinkWizard(models.TransientModel):
    _name = 'copy.link.wizard.feedback'

    link = fields.Char('Link', readonly=True)

    def action_done(self):
        print(self.link, 'link')
        print('done')
