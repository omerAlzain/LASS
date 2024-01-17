{
    'name': "Gestion de l'Assl",
    'version': '1.0',
    'category': 'Association',
    'summary': 'Gestion d une association et des membres',
    'description': 'Ce module permet de gérer une association, les inscriptions des membres et les paiements.',
    'author': 'Omar Alzain',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/member_view.xml',
        'views/menus.xml',
    ],

    'installable': True,
    'application': True,
}


