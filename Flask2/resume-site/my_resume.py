"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = '<p>Héhéhéhé hèhèhèhè à ?</p>'

languages = [
        ['English', ' (OK)'],
        ['French', ' (Fine)'],
        ]

education = [
        ['Degree in ééééééèèèè àà  Data Science and AI Programming', 'Simplon/Microsoft AI School', '2020 - 2021'],
        ['BSc in Applied Mathematics', 'Bristol University', '2007 - 2011']
        ]

interests = ['This Thing', 'that Thing']

skills = [
        ['Python & Flask', '20%'],
        ['R', '1%'],
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
        ['Lead Developer',
            '2015 - Present',
            'Startup Hubs, San Francisco',
            '<p>Did not do much </p>'
        ],
        ['Senior Software Engineer',
            '2014 - 2015',
            'Google, London',
            '<p>Did not do much either</p>'
        ],
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
project_intro = '<p>A few side projects</p>'
projects = [
        ['Tempo',
            'A responsive website template designed to help startups promote their products or services and to attract users &amp; investors.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-startups-tempo/'
        ],
        ['Atom',
            'A comprehensive website template solution for startups/developers to market their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/'
        ],
    ]



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
resume_data = {
    'site_title' : 'CV Bastien',
    'name' : 'Bastien Carniel',
    'tagline' : 'Aspiring Developer',
    'email' : 'bastien.carniel@website.com',
    'phone' : '0123 456 789',
    'website' : 'bastiencarniel.com',
    'linkedin' : 'linkedin.com/in/bastien',
    'github' : 'github.com/bastien',
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience,
    'project_intro' : project_intro,
    'projects' : projects
    }
