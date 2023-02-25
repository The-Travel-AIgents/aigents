# AIgents Backend

## Getting Started

### Installing Dependencies
Step 1
#### Install Python on your Local MAchine

The project makes use of Python 3.8.10 but any Python version > 3.7 will work so you can follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

Step 2

Navigate to the folder you want to work in

Step 3
#### Setup a Virtual Environment in the folder in Step 2

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
python -m venv <name-of-your-environment>
```
To activate the environment on Windows:
```bash
source <name-of-your-environment>/Scripts/activate
```
Step 4
### Initialize git in the folder you are working from
To do this, run:

```bash
git init
```
Step 5
#### clone this repository to your Local machine

Once you have git initialized and your virtual environment setup and active, now you want to get the existing code base from this github repository to your local machine.
Run:

```bash
git clone https://github.com/The-Travel-AIgents/aigents.git
```
This will clone the remote repository to your local machine

Step 6

Navigate to the root folder of the repo you just cloned, i.e the folder containing: `manage.py`

Step 7
#### PIP Dependencies
Once you have successfully cloned the project to your Local machine, now you want to install the dependencies to run the project,
All the dependencies are stored in the requirements.txt file
To install run:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we within the `requirements.txt` file.

## Running the server
First ensure your created virtual environment is active and all dependencies have been installed successfully
From your root directory, i.e within the directory containing `manage.py`

```bash
python manage.py runserver
```
This will detect file changes and run the server automatically.

## Tasks

### TODO

1. 
2. 
3. 
4. 
