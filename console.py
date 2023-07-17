#!/usr/bin/python3

""" Command line interpreter """

import cmd
import models
from models.base_model import BaseModel


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
            if args[0] not in ["BaseModel"]:
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
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            class_name = args[0]
            instance_id = args[1]

            obj_dict = models.storage.all()

            key = f"{class_name}.{instance_id}"

            if key in obj_dict:
                instance = obj_dict[key]
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            class_name = args[0]
            instance_id = args[1]

            obj_dict = models.storage.all()

            del_key = f"{class_name}.{instance_id}"

            if del_key in obj_dict:
                del obj_dict[del_key]

                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        args = arg.split()
        instances = models.storage.all().values()

        if len(args) == 0:
            for instance in instances:
                print(instance)
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist ** ")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            instance = BaseModel()
            class_name == args[0]
            intance_id = args[1]

            if instance.id != instance_id:
                print("** no instance found **")
            else:
                print(instance)

        if len(args) == 1:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
            else:
                for instance in instances:
                    if instance.__class__.__name__ == args[0]:
                        print(instance)

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = arg.split()
        obj = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            key = f"{args[0]}.{args[1]}"
            if key not in obj:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            key = f"{args[0]}.{args[1]}"
            if key not in obj:
                print("** no instance found **")
            else:
                print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in obj:
                print("** no instance found **")
            else:
                attr = args[2]
                val = args[3]
                obj_instance = obj[key]
                data_type = type(val)

                if data_type == int:
                    new_val = int(val)
                    setattr(obj_instance, attr, new_val)
                elif data_type == float:
                    new_val = float(val)
                    setattr(obj_instance, attr, new_val)

                setattr(obj_instance, attr, val)

                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
