#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB's commands"""
    prompt = '(hbnb) '

    def do_create(self, param):
        """Creates a new instance, saves it and print id"""
        if param:
            if param == 'BaseModel':
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            elif param == 'User':
                new_instance = User()
                new_instance.save()
                print(new_instance.id)
            elif param == 'Place':
                new_instance = Place()
                new_instance.save()
                print(new_instance.id)
            elif param == 'State':
                new_instance = State()
                new_instance.save()
                print(new_instance.id)
            elif param == 'City':
                new_instance = City()
                new_instance.save()
                print(new_instance.id)
            elif param == 'Amenity':
                new_instance = Amenity()
                new_instance.save()
                print(new_instance.id)
            elif param == 'Review':
                new_instance = Review()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, param_name):
        """Prints the string representation of an instance
        """
        if param_name:
            my_dict = storage.all()
            line = param_name.split(" ")
            instance_name = line[0]
            if instance_name == 'BaseModel'\
                or instance_name == 'User'\
                or instance_name == 'Place'\
                or instance_name == 'State'\
                or instance_name == 'City'\
                or instance_name == 'Amenity'\
                    or instance_name == 'Review':
                if len(line) == 2:
                    instance_id = line[1]
                    id_list = []
                    for key in my_dict:
                        val = my_dict[key]
                        id_list.append(val.id)
                        if val.id == instance_id and\
                                val.__class__.__name__ == instance_name:
                            print(val)
                        else:
                            print("** no instance found **")
                    if instance_id not in id_list:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, params):
        """Deletes an instance based on class name and id
        """
        if params:
            line = params.split(" ")
            my_dict = storage.all()
            instance_name = line[0]
            if instance_name == 'BaseModel'\
                or instance_name == 'User'\
                or instance_name == 'Place'\
                or instance_name == 'State'\
                or instance_name == 'City'\
                or instance_name == 'Amenity'\
                    or instance_name == 'Review':
                if len(line) == 2:
                    instance_id = line[1]
                    id_list = []
                    for key in my_dict:
                        val = my_dict[key]
                        id_list.append(val.id)
                        if val.id == instance_id and\
                                val.__class__.__name__ == instance_name:
                            key_del = key
                        else:
                            print("** no instance found **")
                    if instance_id not in id_list:
                        print("** no instance found **")
                    else:
                        del my_dict[key_del]
                        for key in my_dict:
                            storage.new(my_dict[key])
                        storage.save()
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, params):
        """Prints all string rep. of all instances of a class
        """
        if params != 'BaseModel'\
            and params != ''\
            and params != 'User'\
            and params != 'Place'\
            and params != 'State'\
            and params != 'City'\
            and params != 'Amenity'\
                and params != 'Review':
            print("** class doesn't exist **")
        else:
            my_dict = storage.all()
            my_list = []
            for key in my_dict:
                my_list.append(str(my_dict[key]))
            print(my_list)

    def do_update(self, params):
        """Updates an instance by updating or adding attribute
        """
        if params:
            line = params.split(" ")
            instance_name = line[0]
            if instance_name == 'BaseModel'\
                or instance_name == 'User'\
                or instance_name == 'Place'\
                or instance_name == 'State'\
                or instance_name == 'City'\
                or instance_name == 'Amenity'\
                    or instance_name == 'Review':
                if len(line) > 1:
                    instance_id = line[1]
                    my_dict = storage.all()
                    my_list = []
                    for key in my_dict:
                        val = my_dict[key]
                        my_list.append(val.id)
                    if instance_id not in my_list:
                        print("** no instance found **")
                    else:
                        if len(line) > 2:
                            attribute_name = line[2]
                            if len(line) > 3:
                                attribute_value = line[3][1:-1]
                                for key in my_dict:
                                    val = my_dict[key]
                                    if instance_id == val.id:
                                        instance_update = val
                                        instance_update.__dict__[
                                            attribute_name] =\
                                            attribute_value
                                        instance_update.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
