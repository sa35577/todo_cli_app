This is a Python CLI to-do list applicaiton. It was kind of inspired by me wanting to experiment with the `Typer` library and `pytest` for the testing environment. Steps to use this project:

1. Download the repo
2. You can run this in a virtual environment (it makes it easier to manage dependencies). In MacOS, this is done with:

```
python -m venv venv
source myenv/build/activate
```
and you should be in your virtual environment, named `venv`.

This can be done in a similar way for Windows.

3. Install dependencies in the virtual environment. Run the following command (inside the virtual environment):

```
python -m pip install -r requirements.txt
```

And now you should be good to go!

Here are the basic functionalities that this app supports:

**Initialize a new to-do list, which will prompt for a directory to store the database (with a default location to use):**
```
python -m rptodo init
```

**Add something to the priority list:**
Default priority is 2, and range is 1-3. Use the `add` keyword, with flag `-p` or `--priority` for the priority field.

```
python -m rptodo add Get food -p 1 
## Get food with priority 1

python -m rptodo add Clean house --priority 3 
## Clean house with priority 3

python -m rptodo add Wash the car
## Wash the car with priority 2

python -m rptodo add Go for a walk -p 5
## Errors out as priority was set outside of range
```

**List all priorities:**

```
python -m rptodo list
```

In this case, the output will be 

```
to-do list:

ID.  | Priority  | Done  | Description
----------------------------------------
1    | (1)       | False | Get food.
2    | (3)       | False | Clean house.
3    | (2)       | False | Wash the car.
----------------------------------------
```

**Complete a command:**
Lists a command as complete. With the previous example, let's say we do
```
python -m rptodo complete 1
```
Then, if we list all priorities, we get:
```
to-do list:

ID.  | Priority  | Done  | Description
----------------------------------------
1    | (1)       | True  | Get food.
2    | (3)       | False | Clean house.
3    | (2)       | False | Wash the car.
```

**Remove from the priority list:**
Will give a confirmation on what the priority to remove will be, with a `[y\N]` keyboard prompt.
The command

```
python -m rptodo remove 1
```
will remove the first entry. Listing all priorities again would result in
```
to-do list:

ID.  | Priority  | Done  | Description
----------------------------------------
1    | (3)       | False | Clean house.
2    | (2)       | False | Wash the car.
```

**Clear priority list:**
Will give a confirmation to delete all to-dos, with a `[y\N]` keyboard prompt. Can use with
```
python -m rptodo clear
```
and trying to list will result in it being empty.


Credit for a lot of the code (to help me learn all of this) to the following tutorial: https://realpython.com/python-typer-cli