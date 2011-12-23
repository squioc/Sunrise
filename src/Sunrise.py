import sys
import argparse
import inspect

class Sunrise(object):
    "A Pythonic command line framework"

    def __init__(self):
        self.argparser = argparse.ArgumentParser(description=self.__doc__)
        self.argparser.add_argument('command', metavar='command', type=str, nargs=1, help='command to execute')
        self.argparser.add_argument('args', metavar='arguments', type=str, nargs='*', help='argumments for the command')

    def add_option(self, name, **kwargs):
        self.argparser.add_argument(('--%s' % name), dest=('opt_%s' % name), **kwargs)

    def usage(self):
        pass

    def command_missing(self, cmd_name, args, options):
        pass

    def do_list_commands(self, args, options):
        """print all available commands"""
        print "list of available commands:"
        print ""

        for method in self._get_all_commands():
            print method.func_name[3:].ljust(20,' '), method.func_doc

    def _get_all_commands(self):
        for method_name in dir(self):
            if method_name.startswith('do_'):
                method = getattr(self, method_name, None)
                if method is not None and inspect.ismethod(method):
                    yield method

    def _parse_args(self, args):
        arguments = self.argparser.parse_args(args)

        arg_options_list = [(opt[4:],getattr(arguments, opt, None)) for opt in dir(arguments) if opt.startswith('opt_')]

        return (arguments.command[0], dict(arg_options_list), arguments.args)

    def run(self, args=sys.argv):
        (command, options, arg_list) = self._parse_args(args)

        cmd_method = 'do_%s' % command
        if hasattr(self, cmd_method):
            func = getattr(self, cmd_method)
            func(arg_list, options)
        else:
            self.command_missing(command, arg_list, options)
