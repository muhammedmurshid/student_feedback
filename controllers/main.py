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


class WebFacultyFeedbackForm(http.Controller):
    @http.route(['/feedback_faculty/<string:batch_id>/<string:user_id>'], type='http', auth="public", website=True)
    def feedback(self, batch_id, user_id, **kw):
        print(batch_id, 'batch_id url')
        decoded_data = int(batch_id, 16)

        print("Decoded data:", decoded_data)

        # bytes_data = base64.b64decode(batch_id)
        # base64_decoded = base64.urlsafe_b64decode(batch_id)
        # print(base64_decoded, 'batch_id bytes')
        # integer_value = int.from_bytes(base64_decoded, byteorder='big', signed=False)
        # base64_decoded = base64.urlsafe_b64decode(integer_value)
        # decodedBytes = base64.b64decode(bytes_data)
        # decodedStr = str(decodedBytes, "utf-8")
        # decoded_data = int(hexadecimal_string, 16)
        #
        # print("Decoded data:", decoded_data)
        decoded_fac_data = int(user_id, 16)

        # bytes_data_user = base64.b64decode(user_id)
        # integer_value_user = int.from_bytes(bytes_data_user, byteorder='big', signed=False)
        # print(integer_value_user, 'integer_value_user')

        batch = request.env['logic.base.batch'].sudo().search([('id', '=', int(decoded_data))])
        user = request.env['res.users'].sudo().search([('id', '=', int(decoded_fac_data))])

        values = {
            'batches': batch,
            'user': user,
            # 'batch_id': batch.id,
            # 'batch_name': batch,
            # 'user_name': user,
            # 'user_id': user.id

        }
        print("feedback")
        return request.render("student_feedback.faculty_feedback_form_template", values)

    @http.route(['/feedback_faculty/submit'], type='http', auth="public", website=True, csrf=False)
    def create_data_feedback(self, **post):
        print("create_data_feedback")
        print(post)
        request.env['faculty.feedback'].sudo().create({
            'student_name': post.get('student_name'),
            'faculty_name': post.get('faculty_id'),
            'batch_id': post.get('batch_id'),
            'clarity_of_topics': post.get('clarity_of_topics'),
            'pace_of_class': post.get('pace_of_class'),
            'explanation_of_theory_topics': post.get('explanation_of_theory_topics'),
            'explanation_of_problem_question': post.get('explanation_of_problem_question'),
            'any_further_suggestions': post.get('feedback_name'),

        })

        return request.render('student_feedback.tmp_faculty_feedback_form_thanks')
