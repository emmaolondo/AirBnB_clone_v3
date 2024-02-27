#!/usr/bin/python3

class TestConsole(unittest.TestCase):
    """Test the console module"""

    def test_do_create(self):
        """Test do_create"""
        with redirect_stdout(self.output):
            self.cmdcon.onecmd('create')
            self.assertEqual(self.output.getvalue(),
                             "** class name missing **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create blah')
            self.assertEqual(self.output.getvalue(),
                             "** class doesn't exist **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State name="California"')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing DBStorage")
    def test_do_create_db(self):
        """Test do_create"""
        with redirect_stdout(self.output):
            self.cmdcon.onecmd('create')
            self.assertEqual(self.output.getvalue(),
                             "** class name missing **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create blah')
            self.assertEqual(self.output.getvalue(),
                             "** class doesn't exist **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State name="California"')
            id = self.output.getvalue()
            self.assertRegex(id,
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
