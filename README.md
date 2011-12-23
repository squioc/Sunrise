
**Sunrise** is a pythonic command line framework to ease development of command line utilities.
It depends on [argparse](http://code.google.com/argparse/) for arguments parsing.

In order to create your own command line utility, you have to inherit from Sunrise class.
For each command you want from your command line utility, create a *'do_\<command_name\>'* method.
it must accept two arguments:

- a list of arguments passed throw the command line
- a dictionnary of options your utility accepts

Example:

    import Sunrise
    import os

    Class Heroku(Sunrise.Sunrise):
        def do_herokize(self, args, options):
            os.makedir(args[1])
            os.chdir(args[1])
            open('.gitignore','w+').write('*.pyc')
            open('Procfile').write('web: python manage.py gunicorn')
            open('requirements.txt','w+').write('')


To add an additional option, in your utility, call *'add_option'* method in the *'\_\_init\_\_'* method.

    Class Heroku(Sunrise.Sunrise):
        def __init__(self):
            super(Heroku, self).__init__()
            self.add_option('<option_name'>, <options_parameter>)

See [argparse's add\_argument method](http://argparse.googlecode.com/svn/trunk/doc/add_argument.html) to know available parameters for *'\<option_parameter\>'*
