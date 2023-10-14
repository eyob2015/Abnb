#!/usr/bin/env python3
import cmd
import sys
import models
from models.user import User
from models import file_storage
import json
from base_model import BaseModel
from user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import  Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    
    
    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if not arg:
            instances = models.storage.all().values()
        else:
            class_name = arg
            if class_name not in models.classes:
                print("** class doesn't exist **")
                return
            instances = [v for k, v in models.storage.all().items() if class_name in k]

        print([str(instance) for instance in instances])

    def do_show(self, arg):
        """Show the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = args[0] + '.' + obj_id
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_create(self, arg):
        """Create a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        new_obj = models.classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = args[0] + '.' + obj_id
        objects = storage.all()
        if key in objects:
            objects.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Update an instance based on the class name and id with a dictionary"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** dictionary missing **")
            return
        obj_id = args[1]
        key = args[0] + '.' + obj_id
        try:
            dictionary = eval(args[2])
            if not isinstance(dictionary, dict):
                raise ValueError
        except (NameError, SyntaxError, ValueError):
            print("** invalid dictionary **")
            return
        objects = storage.all()
        if key in objects:
            obj = objects[key]
            for attr, value in dictionary.items():
                setattr(obj, attr, value)
            obj.updated_at = datetime.now()
            storage.save()
        else:
            print("** no instance found **")


    def do_all(self, arg):
        """Retrieve all instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        all_instances = storage.all(models.classes[args[0]])
        print(all_instances)
    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        count = storage.count(models.classes[args[0]])
        print(count)



if __name__ == '__main__':
    HBNBCommand().cmdloop()