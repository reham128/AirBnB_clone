#!/usr/bin/python3
"""console module that represent the entry point to the app"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class to handel the command line interpretr to act like the
    front-End for the AirBnB clone"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """to exit the program"""
        return (True)

    def do_quit(self, line):
        """to quit the program"""
        return (True)

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """to create new instance and save it to json file"""
        pass

    def do_show(self, line):
        """Prints the string representation of an instance"""
        pass

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        and save the changes to the json file"""
        pass

    def do_all(self, line):
        """to print all instances of based or not on the class name"""
        pass

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
