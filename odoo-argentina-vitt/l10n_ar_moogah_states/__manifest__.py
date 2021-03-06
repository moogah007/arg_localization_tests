# -*- coding: utf-8 -*-
{
    "name": "Provincias Argentinas con Cod. AFIP",
    'version': '10.0.1.2',
    'category': 'Localization/Argentina',
    'author': 'Moogah',
    'license': 'AGPL-3',
    'summary': """App de actualizacion para cod. AFIP en Provincias""",
    'description': """
        App que actualiza el campo para el codigo AFIP en las provincias de Argentina.
        """,
    
    'depends': ['base',
    			'l10n_ar_states',
    ],
    'data': ['data/res.country.state.csv'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
