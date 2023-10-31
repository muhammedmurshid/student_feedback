{
    'name': "Students Feedback",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/feedback_rules.xml',
        'views/feedback.xml',
        'views/wb_form.xml',
        'views/link_menu.xml',
        'views/wizard.xml',
        'views/faculty_feedback.xml',
        'views/faculty_feedback_link.xml',
        'views/web_form_fac_feedback.xml',
        # 'views/assets.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'student_feedback/static/src/js/custom_widget.js'],
    },
    'demo': [],
    'summary': "logic_students_feedback",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
