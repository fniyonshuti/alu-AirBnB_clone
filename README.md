# AirBnB Clone - The Console

## Project Description
This project is the first step towards building a full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Command Interpreter Description
The command interpreter is designed to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file
- Update attributes of an object
- Destroy an object

### How to start it
To start the command interpreter, run the following command:

```
python ./console.py
```

### How to use it
The command interpreter can be used in:

#### Interactive Mode
In interactive mode, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit all  create  destroy  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```



### Commands
The commands available in the interpreter are:

- `create`: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
- `show`: Prints the string representation of an instance based on the class name and id.
- `destroy`: Deletes an instance based on the class name and id.
- `all`: Prints all string representation of all instances based or not on the class name.
- `update`: Updates an instance based on the class name and id by adding or updating attribute.
- `quit`: Exits the program.
- `EOF`: Exits the program.

### Examples
```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
$
```

