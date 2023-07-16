#!/usr/bin/python3

""" Command line interpreter """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Command line interpreter """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ Exits program cleanly """
        return True

    def emptyline(self):
        """Do nothing when the user enters an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
