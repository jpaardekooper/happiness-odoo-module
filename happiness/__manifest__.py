# -*- coding: utf-8 -*-
{
    'name': 'Happiness Flow',
    'version': '14.0.2.0',
    'summary': 'Happiness Flow',
    'sequence': -1,
    'description': """Happiness Flow""",
    'category': 'Monitoring',
    'website': '',
    'license': 'LGPL-3',
    'depends': ["base", "hr"],
    'data': [
        'security/happiness_security.xml',
        'security/ir.model.access.csv',       
        'views/conversation.xml',
        'views/response.xml',      
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
