from Sunrise import Sunrise

class Test(Sunrise):
    def __init__(self):
        super(Test, self).__init__()
        self.add_option('single', nargs=1, type=str)
        self.add_option('multiple', nargs=2, type=str)

    def do_hello(self, args, options):
        print "hello"

    def do_bye(self, args, options):
        print "bye"

    def get_all_commands(self):
        return self._get_all_commands()

    def parse_args(self, args):
        return self._parse_args(args)
