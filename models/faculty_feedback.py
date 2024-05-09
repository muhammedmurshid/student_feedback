from odoo import api, fields, models, _
import base64


class FacultyFeedbackForm(models.Model):
    _name = 'faculty.feedback'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Faculty Feedback'
    _rec_name = 'student_name'

    student_name = fields.Char(string='Student Name')
    faculty_name = fields.Many2one('res.users', string='Faculty Name')
    batch_id = fields.Many2one('logic.base.batch', string='Batch')
    clarity_of_topics = fields.Selection(
        [('none', 'None'), ('poor', 'Poor'), ('average', 'Average'), ('good', 'Good'), ('excellent', 'Excellent')],
        string='Clarity of Topics'
    )
    pace_of_class = fields.Selection(
        [('none', 'None'), ('very_slow', 'Very Slow'), ('slow', 'Slow'), ('normal', 'Normal'), ('fast', 'Fast')], string='Pace of Class'
    )
    explanation_of_theory_topics = fields.Selection(
        [('none', 'None'), ('poor', 'Poor'), ('average', 'Average'), ('good', 'Good'), ('excellent', 'Excellent')],
        string='Explanation of Theory Topics'
    )
    explanation_of_problem_question = fields.Selection(
        [('none', 'None'), ('poor', 'Poor'), ('average', 'Average'), ('good', 'Good'), ('excellent', 'Excellent')],
        string='Explanation of Problem Question'
    )
    any_further_suggestions = fields.Text(string='Any Further Suggestions')
    company_id = fields.Many2one(
        comodel_name='res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company.id
    )

    def current_url_link_feedback_faculty(self):
        company = self.env['res.company'].search([('id', '=', self.env.company.id)])
        return {'name': _('Faculty Feedback Link'),
                'type': 'ir.actions.act_window',
                'res_model': 'faculty.feedback.link',
                'view_mode': 'form',
                'target': 'new',

                }


class FeedbackLink(models.TransientModel):
    _name = 'faculty.feedback.link'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Feedback Link'

    link = fields.Char(string='Link', compute='_action_copy_link')
    faculty_id = fields.Many2one('res.users', string='Faculty', domain=[('faculty_check', '=', True)])
    batch_id = fields.Many2one('logic.base.batch', string='Batch')

    @api.depends('faculty_id', 'batch_id')
    def _action_copy_link(self):
        batch = self.batch_id.id
        hexadecimal_string = hex(batch)

        print("Encoded data:", hexadecimal_string)

        # byte_value = batch.to_bytes((batch.bit_length() + 7) // 8, byteorder='big')
        # print(byte_value, 'batch byte value')
        # base64_encoded = base64.b64encode(byte_value).decode('utf-8')
        base64_encoded = hex(batch)
        print(base64_encoded, 'batch_number')

        faculty = self.faculty_id.id
        hexadecimal_fac_string = hex(faculty)
        byte_value_fac = faculty.to_bytes((faculty.bit_length() + 7) // 8, byteorder='big')
        # base64_encoded_fac = base64.b64encode(byte_value_fac).decode('utf-8')
        base64_encoded_fac = hexadecimal_fac_string

        company = self.env['res.company'].search([('id', '=', self.env.company.id)])
        self.link = company.website + '/' + 'feedback_faculty' + '/' + str(base64_encoded) + '/' + str(base64_encoded_fac)


    def action_copy_link(self):
        print('hi')
