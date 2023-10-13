#!/usr/bin/python3
""" AirBnB console using cmd"""

import json
import cmd
import models
from models.base_model import BaseModel
from models import storage, all_classes

class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = "(hbnb) "
    

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True
    
    def do_create(self, line):
        "Creates a new instance of BaseModel"
        if len(line) == 0:
            print("** class name missing **")
            return
        
        args = line.split(" ")        
        for key in all_classes.keys():
            if args[0] != key:
                print("** class doesn't exist **")
            else:
                instance = all_classes[args[0]]()
                instance.save()
                print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class name and id
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        
        args = line.split(" ")
        if not args[1]:
                print("** instance id missing **")
        else:
            instance = "{}.{}".format(args[0], args[1])
            for key, values in storage.all().items():
                if key == instance:
                    print(values)
            if instance not in storage.all().keys():
                print("** no instance found **")
            
        if args[0] not in storage.all_classes.keys():
            print("** class doesn't exist **")
    
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        if len(line) <= 1:
            print("** instance id missing **")
            return
        
        args = line.split(" ")

        if args[0] not in storage.all_classes.keys():
            print("** class doesn't exist **")

        instance="{}.{}".format(args[0], args[1])
        if instance in storage.all().keys():
            del storage.all()[instance]
            storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, line):
        """
        Prints all string representation of
        all instances based or not on the class name
        """
        inst_list = []
        args = line.split(" ")

        
        if len(line) == 0:
            for item in storage.all().values():
                inst_list.append(str(item))
            print(inst_list)
            return

        if args[0] in storage.all_classes.keys():
            for key, value in storage.all().items():
                if key.split(".")[0] == args[0]:
                    inst_list.append(str(value))
            print(inst_list)
            return
        else:
            print("** class doesn't exist **")
            return
            
        
        

        








if __name__ == '__main__':
    HBNBCommand().cmdloop()
