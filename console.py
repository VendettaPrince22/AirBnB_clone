#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd

if __name__ == '__main__':
    class HBNBCommand(cmd.Cmd):
        """Defines the HBNB's commands"""
        prompt = '(hbnb) '

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
