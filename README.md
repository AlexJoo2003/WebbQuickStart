# Webb Quick Start

A small little script to get you ready for coding a website on the go. This will create for you index.html, style.css, script,js in an orgonized way with only one command. You could also choose to add Bootstrap cdn and/or JQuery cdn. It could also add some extra folders and sass on your command

> Disclaimer! This is my personal preferences, and you might not like my layot of the files or how I name my files.
---
### How to install

Clone the repositry
    
    $ git clone https://github.com/AlexJoo2003/WebbQuickStart.git
Then move your file to where ever you want and make an alias. Thats all you need.

### How to use it

Basic syntax:
Name of your project is always first, the name is not allowed to have any spaces in it. The name will be your index.html title value
```
    $ py webbqs.py Name-Of-Your-Project -arg -arg -arg
```
There are several arguments for special settings which are not neccesery. If no arguments are used there will only be created index.html, style.css and script.js

##### Arguments

* -b adds bootstrap
* -j adds jquery
* -s adds sass
* -i adds image folder
* -f adds image folder

> The CDNs for bootstrap and jquery are not automaticly updated! yet...

### How to uninstall 

Delete the file and remove the alias
