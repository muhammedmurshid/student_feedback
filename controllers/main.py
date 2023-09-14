from odoo import http
from odoo.http import request
import base64


class WebStudentFeedbackForm(http.Controller):
    @http.route(['/feedback/<string:user_id>'], type='http', auth="public", website=True)
    def feedback(self, user_id, **kw):
        decoded_bytes = base64.b64decode(user_id)
        user_id = int.from_bytes(decoded_bytes, byteorder='big')
        batch = request.env['logic.base.batch'].sudo().search([])
        user = request.env['res.users'].sudo().browse(user_id)
        values = {
            'batches': batch,
            'id': user.id,
            'name': user.name,
        }
        print("feedback")
        return request.render("student_feedback.feedback_form_template", values)

    @http.route(['/feedback/submit'], type='http', auth="public", website=True, csrf=False)
    def create_data_feedback(self, **post):
        print("create_data_feedback")
        rating = int(post.get('stars', 0))
        print(post.get('feedback_name'), 'feed')
        print(post.get('coordinator'), 'coor')

        request.env['student.feedback'].sudo().create({
            'student_name': post.get('student_name'),
            # 'coordinator_id': post.get('coordinator_id'),
            'batch_id': post.get('batch_id'),
            'feedback': post.get('feedback_name'),
            'star_rating': str(rating),
            'coordinator_id': post.get('coordinator'),



        })
        return request.render('student_feedback.tmp_student_feedback_form_thanks')
        # print("create_data_feedback")
        # here in kw you can get the inputted value
