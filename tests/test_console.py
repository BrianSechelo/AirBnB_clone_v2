#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage

class TestHBNBCommand(unittest.TestCase):
    """Unittest for testing the HBNB command interpretter."""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing set up.
        Temporarily rename any existing file.json
        Reset all file objects
        Create an instance of the COmmand interpretter"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing tear down
        restore original file.json.
        Delete the test HBNBCommand instance.
        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        """Reset filestorage objects dictionary."""
        FileStorage._FileStorage_objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create_for_errors(self):
        """Test Create Command Errors."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                    "** class name missing **\n", f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual(
                    "** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
        """Test create comamnd."""
        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create Base_Model")
             bm = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create User")
             us = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create State")
             st = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create Place")
             pl = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create City")
             ct = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create Review")
             rv = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("create Amenity")
             am = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all BaseModel")
             self.assertIn(bm = f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all user")
             self.assertIn(us = f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all State")
             self.assertIn(st = f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all Place")
             self.assertIn(pl = f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all City")
             self.assertIn(ct = f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all Review")
             self.assertIn(rv = f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
             self.HBNB.onecmd("all Amenity")
             self.assertIn(am = f.getvalue().strip())

    def test_create_command_with_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as f:
            call = (f'create Place city_id="0001" user_id="0001" name="My_house" number_rooms=4 latitude=37.77 longitude=43.434')
            self.HBNB.onecmd(call)
            pl =  f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001", output)
            self.assertIn("'name': 'My house", output)
            self.assertIn("'number_rooms': '4", output)
            self.assertIn("'latitude': '37.77", output)
            self.assertIn("'longitude': '43.434", output)
    if __name__ == "__main__":
        unittest.main()
