## AirBnB Clone - The Console

### Description
This is a full web application of the AirBnb Clone. It consists of the console, web static, mySQL storage, web framework(templating), RESTful API, Web dynamic.
This is the first stage which involves building the command interpreter

### The Command interpreter (console)
The Console is built using the ```cmd``` module.
The program ```console.py``` which contains the entry point to the command interpreter has the class definition ```class HBNBCommand(cmd.Cmd):``` 
The command interpreter implements:
- ```quit``` and ```EOF``` to exit the program
- ```help```
- a custom prompt ```(hbnb)```
- an empty line + ```ENTER``` doesn't execute anything

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
