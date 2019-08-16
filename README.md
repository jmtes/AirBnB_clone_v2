# HBNB - Airbnb Clone
<p align="center">
  <img src="https://i.imgur.com/ogbfW3k.png">
</p>
This is a simple copy of the AirBnB website meant to instill the fundamental concepts of high-level programming.

## The Console
This is a command line interpreter that aids the storing/managing/manipulating of site data for development and debugging.
### Starting the Console
Upon cloning or downloading the repo, simply `cd` into the `AirBnB_clone` directory and run `console.py`. You should be able to see the prompt `(hbnb) `.
```
vagrant$ cd AirBnB_clone/
AirBnB_clone$ ./console.py
(hbnb) 
```
```
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
And in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $
```
#### Command Overview

| Command        | Function           | Usage |
| ------------- |-------------| ------------- |
| `create` | Create object and display its id | `create <OBJ TYPE>` |
| `show` | Show object info      | `show <OBJ TYPE> <OBJ ID>` |
| `destroy` | Delete object      | `destroy <OBJ TYPE> <OBJ ID>` |
| `all` | Show all objects      | `all [OBJ TYPE]` |
| `update` | Update object attribute      | `update <OBJ TYPE> <OBJ ID> <ATTR NAME> <ATTR VALUE>` |
| `help` | Display command info      | `help [COMMAND]` |
| `quit`, `EOF` | Exit the console      | `quit` |

* Required command arguments are denoted with `< >`. Optional arguments are denoted with `[ ]`.
* `OBJ TYPE` can be one of the following: `BaseModel`, `User`, `State`, `City`, `Place`, `Amenity`, `Review`
* `OBJ ID` refers to each object's unique ID, which is stored in its `id` attribute.
* `COMMAND` can be any one of the above commands.

#### Examples
* To create a `City` object, display its info, and delete it:
```
AirBnB_clone$ ./console.py
(hbnb) create City
783b144c-2b43-42c5-9945-e089c966cd9d
(hbnb) show City 783b144c-2b43-42c5-9945-e089c966cd9d
[City] (783b144c-2b43-42c5-9945-e089c966cd9d) {'id': '783b144c-
2b43-42c5-9945-e089c966cd9d', 'updated_at': datetime.datetime(2019, 7, 2, 19, 
57, 29, 868183), 'created_at': datetime.datetime(2019, 7, 2, 19, 57, 29, 
867862)}
(hbnb) destroy City 783b144c-2b43-42c5-9945-e089c966cd9d
(hbnb) show City 783b144c-2b43-42c5-9945-e089c966cd9d
** no instance found **
(hbnb) 
```
* To display all working instances:
```
(hbnb) all
["[City] (06179065-4084-4a4b-88e5-c67d9832bf71) {'created_at': 
datetime.datetime(2019, 7, 2, 20, 5, 52, 63134), 'updated_at': 
datetime.datetime(2019, 7, 2, 20, 5, 52, 63134), 'id': '06179065-4084-4a4b-
88e5-c67d9832bf71', '__class__': 'City'}", "[User] (bba5b797-d8e3-42e3-
aa43-10826d06ba39) {'created_at': datetime.datetime(2019, 7, 2, 20, 5, 47, 
863451), 'updated_at': datetime.datetime(2019, 7, 2, 20, 5, 47, 863688), 
'id': 'bba5b797-d8e3-42e3-aa43-10826d06ba39', '__class__': 'User'}", "[Place] 
(1215e087-0c08-4795-9528-566c111278bb) {'created_at': datetime.datetime(2019, 
7, 2, 20, 5, 54, 664432), 'updated_at': datetime.datetime(2019, 7, 2, 20, 5, 
54, 665353), 'id': '1215e087-0c08-4795-9528-566c111278bb', '__class__': 
'Place'}", "[Place] (640fb953-9b25-4ab0-ba8f-2be34b887f9d) {'created_at': 
datetime.datetime(2019, 7, 2, 20, 5, 57, 214700), 'updated_at': 
datetime.datetime(2019, 7, 2, 20, 5, 57, 214700), 'id': '640fb953-9b25-4ab0-
ba8f-2be34b887f9d', '__class__': 'Place'}"]
(hbnb) 
```
* To display all working instances of the `Place` class:
```
(hbnb) all Place
["[Place] (1215e087-0c08-4795-9528-566c111278bb) {'created_at': 
datetime.datetime(2019, 7, 2, 20, 5, 54, 664432), 'updated_at': 
datetime.datetime(2019, 7, 2, 20, 5, 54, 665353), 'id': 
'1215e087-0c08-4795-9528-566c111278bb', '__class__': 'Place'}", "[Place] 
(640fb953-9b25-4ab0-ba8f-2be34b887f9d) {'created_at': datetime.datetime(2019, 
7, 2, 20, 5, 57, 214700), 'updated_at': datetime.datetime(2019, 7, 2, 20, 5, 
57, 214700), 'id': '640fb953-9b25-4ab0-ba8f-2be34b887f9d', '__class__': 
'Place'}"]
(hbnb) 
```
* To update the `name` attribute of a `User` object:
```
(hbnb) create User
4728ae45-f208-4093-82d4-dfd8ba7b4e25
(hbnb) show User 4728ae45-f208-4093-82d4-dfd8ba7b4e25
[User] (4728ae45-f208-4093-82d4-dfd8ba7b4e25) {'updated_at': 
datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'created_at': 
datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'id': '4728ae45-
f208-4093-82d4-dfd8ba7b4e25'}
(hbnb) update User 4728ae45-f208-4093-82d4-dfd8ba7b4e25 name 'juno'
(hbnb) show User 4728ae45-f208-4093-82d4-dfd8ba7b4e25
[User] (4728ae45-f208-4093-82d4-dfd8ba7b4e25) {'updated_at': 
datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'name': 'juno', 
'created_at': datetime.datetime(2019, 7, 2, 20, 18, 34, 592964), 'id': 
'4728ae45-f208-4093-82d4-dfd8ba7b4e25'}
(hbnb) 
```
* To show documented commands and get information on the `quit` command:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help quit
 Quit command to exit the program. 
(hbnb) 
```
* To exit the console:
```
(hbnb) quit
AirBnB_clone$ 
```

### The Base Model
To see the file cd to models/base_model.py
Defines all common methods and attributes of future classes and objects.
Public instance attributes:
- id: string: Generates a unique uuid when a BaseModel instance is created.
- created_at: Contains date and time information of an instance when it is first created.
- updated_at: Contains date and time information of an instance when it is updated.
Methods:
- __str__: prints: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
- save(self): updates the public instance attribute updated_at with the current datetime
- to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
  
  
There are two types of file storage engines used in this project: file storage and database storage
### File Storage
To see file cd to models/engines/file_storage.py.
This file storage uses serialization and deserialization processes to store objects. Implemented in: `file_storage.py`
Data flow of the serialization to desearialization process:
`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`
Private class attributes:
- __file_path : string path to the JSON file (ex: file.json)
- __objects: dictionary will store all objects by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
Public instance methods:
- all(self): returns the dictionary __objects
- new(self, obj): sets in __objects the obj with key <obj class name>.id
- save(self): serializes __objects to the JSON file (path: __file_path)
- reload(self): deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)

### Database Storage
Class named DBStorage that uses SQLAlchemy to save objects as records in a database.
To find file cd to models/engines/db_dev_storage.py
Private class attributes:
- __engine: connection to the mysql database
- __session: session that links to the mysql database and storess the changes
Public instance methods:
- all(self, cls=None): returns the dictionary of __objects. Cls represents a specified class to which all instances are returned.
- new(self, obj): Adds the object to the current database session
- save(self): commits all changes of the current database session
- delete(self, obj=None): deletes from the current database session obj if not None
- reload(self): creates all tables in the database (starts session)


### Supported classes:
Additional classes that inherit from BaseModel and Base:

Class Name | Attributes
-- | --
`User` | email, password, first_name, last_name, places, reviews
`Amenity` | Name, place_amenities
`Review` | place_id, user_id, text
`State`  | Name, cities
`City` | state_id, name, places
`Place` | city_id, user_id, name, description, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids, place_amenity, reviews, amenities

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

### About
Created on Ubuntu 14.04 LTS. Using python3 version 3.4.3.

### Authors
* **Sofia Cheung** - [Svcg17](https://github.com/Svcg17)
* **Julienne Tesoro** - [Julienne Tesoro](https://github.com/jmtes)
