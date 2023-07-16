#!/usr/bin/python3

""" Command line interpreter """

import cmd
from  models.base_model import BaseModel

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

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            instance = BaseModel()
            class_name = args[0]
            instance_id = args[1]

            if instance.id != instance_id:
                print("** no instance found **")
            else:
                print(instance)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
