# AirBnB Clone - The Console

## Description
This is a full web application of the AirBnb Clone. It consists of the console, web static, mySQL storage, web framework(templating), RESTful API, Web dynamic.
This is the first stage which involves building the command interpreter

## The Command interpreter (console)
The Console is built using the ```cmd``` module.
The program ```console.py``` which contains the entry point to the command interpreter has the class definition ```class HBNBCommand(cmd.Cmd):``` 
The command interpreter implements:
- ```quit``` and ```EOF``` to exit the program
- ```help```
- a custom prompt ```(hbnb)```
- an empty line + ```ENTER``` doesn't execute anything

#### Execution
In interactive mode:
```$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In non-interactive mode:
```$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
#### Commands available in the command interpreter
| Command | Description |
|---------|-------------|
| create  | Creates a new instance of ```BaseModel```, saves it (to the JSON file) and prints the id. ```Ex: $ create BaseModel``` |
| show    | Prints the string representation of an instance based on the class name and ```id```. ```Ex: $ show BaseModel 1234-1234-1234``` |
| destroy  | Deletes an instance based on the class name and ```id``` (save the change into the JSON file). ```Ex: $ destroy BaseModel 1234-1234-1234```.|
| all      | Prints all string representation of all instances based or not on the class name. ```Ex: $ all BaseModel``` or ```$ all```.|
| update    | Updates an instance based on the class name and ```id``` by adding or updating attribute (save the change into the JSON file). ```Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"```. |

## Models

## Contributors
- Gilbert Malova - malovagilbert@gmail.com - [Github](https://github.com/maloPRO)
- Jesca Chimweri - jessicahchimweri@gmail.com - [Github](https://github.com/chirindo)
