# Building Python Packages
## What are python packages and their benefits
### Structure

- step 1 `create an app folder`
- step 2 inside app folder create`__init__.py`, empty to initialise package
- step 3 inside app folder `fizzbuzz.py`, create functionality
- step 4 `program.py` on directory level, to use as our run file (sometimes called `main.py` or `run.py`)
- step 5 create `setup.py` on directory level to install package, to describe our module details such as version, author and contact details

```
eng89_building_python_packages
- app
-- __init.py__
-- fizzbuzz.py
program.py
setup.py
```

- `fizzbuzz.py` code was copied from previous task and updated to be a function
- `program.py` file code:
```python
from app.fizzbuzz import Fizzbuzz

one_to_100 = Fizzbuzz(100)
print(one_to_100.fizzbuzz_list)

```
- `setup.py` file code:
```python
from setuptools import setup

# add some information about package
setup(name="app") # this is required, lines below are optional
version = "1.0"
description = "Python app"
author = "Tom at Sparta Global"
author_email = "twilliams@spartaglobal.com"
url = "http://spartaglobal.com"
```