# PyOs Documentation
### Contents
1. Installation
    - With Replit
    - Without Replit
2. Using PyOs
   - Basic Features
   - Customizations
3. Writing apps for PyOs
     - Required imports
     - Antivirus issues
     - System libraries
# Installation
There are many ways to run PyOs, but the main options are to use Replit, or use your Terminal.

Replit is mainly used in situations where you may not have an easy time to use the terminal. It is slower as it is hosted on a server, but you don't have to do much to run it.

The terminal is mainly used in situations where you can easily use the terminal or have bad internet.

### With Replit
To install PyOs with Replit, go to the official [PyOs Replit](https://replit.com/@NicholasKarneye/PyOs) and fork it.

![](/images/fork.png)

And tada! Your PyOs installation is complete! Now just click the run button and you should be able to use PyOs.

### Without Replit
To install PyOs without Replit, go to the [GitHub repo](https://github.com/RandomHuman97/PyOs) and download PyOs as a zip file.

![](/images/download.png)

Then, unzip the file. Now, open up whatever terminal you use and type:
```
cd /path/to/pyos
```
(Change the path to whatever file path you have PyOs installed in)
```
python main.py
```
Tada! Now you should see PyOs run. 

If not, make sure you have [Python](https://www.python.org/) installed. If that still doesn't work, make sure you are in the same directory as where the PyOs files are located.
# Using PyOs
PyOs (or just Pyos) is a faux operating system designed to give a semi-graphical interface to Python. This makes it much more user friendly, but it still has a slight learning curve.
### Basic Features
When you first boot PyOs, you'll see something like this

![](/images/image.png)

Now don't be scared, this is just the task-switcher (It's a bad name, I know.)
The purpose of the task-switcher is to give you a quick way to go to wherever you want to go.

Here you can see 3 options, start, apps, and exit.

#### Start
The start screen allows you to go to, the start screen. It doesn't do much right now.
#### Apps
Apps allows you to run apps (explained later).
#### Exit
It, suprisingly, exits PyOs.

To run one of these options, just type the number left of the option (ie: 0 for start).

#### Apps
![](/images/apps.png)

To run apps in PyOs, just type in the filename (make sure to end it in .py)
If the app doesn't show up in the file list, make sure that the file ends in .py
### Customizing PyOS
PyOs uses [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code) to add color to the GUI. To allow customizations, PyOs uses a single python file with all of the system colors, and recommends that PyOs apps do it as well. 
To modify your colors, open the system file pc.py. If all goes well, you should see this.
```python
theme = 0
#pyos default
if theme == 0:
  RED = "\033[0;31m"
  YELLOW = "\033[0;33m"
  CYAN = "\033[0;36m"
  GREEN = "\033[0;32m"
  PURPLE = "\033[35m"
  BLUE = "\033[0;34m"
  BLACK = "\033[0;30m"
  WHITE = "\033[0;37m"
  PINK = "\033[0;95m"
  GREY = "\033[0;90m"
  LIME = "\033[0;92m"
  ENDCOLOR = "\033[0;0m"
#pyos developer
if theme == 1:
  RED = "\033[0;35m"
  YELLOW = "\033[0;93m"
  CYAN = "\033[0;96m"
  GREEN = "\033[0;92m"
  PURPLE = "\033[35m"
  BLUE = "\033[0;34m"
  BLACK = "\033[0;30m"
  WHITE = "\033[0;37m"
  PINK = "\033[0;95m"
  GREY = "\033[0;90m"
  LIME = "\033[0;92m"
  ENDCOLOR = "\033[0;0m"
#colors ^^^
```
Now, you could replace one of the colors on the current themes, but it's highly recommended that you make a new theme.

To make a new theme, first copy the code below and paste it into the pc.py file.
```python
if theme == #theme number:
  RED = "\033[0;31m"
  YELLOW = "\033[0;33m"
  CYAN = "\033[0;36m"
  GREEN = "\033[0;32m"
  PURPLE = "\033[35m"
  BLUE = "\033[0;34m"
  BLACK = "\033[0;30m"
  WHITE = "\033[0;37m"
  PINK = "\033[0;95m"
  GREY = "\033[0;90m"
  LIME = "\033[0;92m"
  ENDCOLOR = "\033[0;0m"
```
Then, change the theme number comment to whatever number you want your theme to use. Make sure that the number is not used by any other themes.

Finally, change the theme variable at the very top of the pc.py file to whatever theme number you want to use. For example, if I wanted to make the current theme 23, I'd type this.
``` python
theme = 23
```
Now that your theme has been created and set, just restart PyOs and the changes should apply.
# Writing Apps for PyOs
PyOs allows users to write apps, using python. There is not much of a learning gap if you already know python, but there are a few quirks you need to know.
### Required Imports
Due to the method of execution PyOs uses to run apps, some imports are required.

The only main import you really need is OS. If you haven't imported a package into your python file before, just add
```python
import os
```
#### Make sure ***NOT*** to import os as another name, it will trigger the antivirus.
Do:
```python
import os
```
Don't do:
```python
import os as bob
```
### Using User Colors
Pyos has a user colors file, named pc.py. This allows your app to stay consistent with the user colors.

To access the colors, just type
```python
import pc
```
When you want to reference  a user color, just type pc. followed by a valid color name.
```python
pc.RED #Default value is red
pc.BLUE #Default value is blue
```

### Antivirus Issues
*Help it's saying that the code has a virus!*

PyOs has a built in simple antivirus. It's main goal is to stop users from accidentally running code that ruins their system (thus saving me alot of complaints).

However, sometimes certain code will trigger the antivirus, which this section will help you avoid.

#### What you can't do =(
- Importing any encryption api's (This will be removed soon when we can detect file writes)
-  Deleting files
-  Deleting folders
-  Writing to files (soon)
- Import the OS module as any other alias

Most of the times you can find a work-around, but if not, you're just kind of screwed at the moment.
### System Libraries
PyOs has a variety of system libraries for apps to use. Here is a simple list of them:

#### ***lib_os***
All of the functions from the lib_os file:
#### mainheader()
Prints the PyOs header. Like this:

![](/images/image.png)

#### taskinp()
Runs the task-switcher.

#### exitfile()
Exit the current file and return back to PyOs
#### safescan(file)
Runs an antivirus scan on the *file* parameter.
If a malicious program is detected, the OS will halt.
#### ***lib_exformat***
All of the functions from the lib_exformat file, these functions are mainly used for extra formatting.
#### linespace(amount)
Prints a certain amount of linespaces, based on the *amount* parameter

## The end.
Self explanatory.
