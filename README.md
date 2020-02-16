# LX_Task4
## About project
The program:
* creates tables of students and rooms
* fills tables with data from `rooms.json`, `students.json`
* runs queries with data from tables
* writes results of queries to xml/json files

## How to run
To run the program from Terminal you need to open it, point interpreter,
script `manager_db.py` and parameters:
* path to `students.json` file
* path to `rooms.json` file
* output format

_Example:_
```
$ python3 manager_db.py '/Users/BruceBanner/work/university/input_files/students.json'
'/Users/BruceBanner/work/university/input_files/rooms.json' xml
```

This program works with MySQL database, so **pay attention** that 
before you run the program the database `LX_Task4` should be
created on you computer (`username='tonystark', 
password='morgan3000'`).