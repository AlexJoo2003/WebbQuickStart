import os
import re
import sys

# Declarations

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link src="css/style.css">
</head>
<body>

    
<script src="scripts/script.js">
</body>
</html>
'''

bootstrap = {
    '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">',
    '<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>',
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>',
    '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>'
}

jquery = {'<script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>', '''
$(document).ready(function(){

});
'''}

available_flags = {"--jquery", "-j",  "--sass", "-s", "--bootstrap", "-b", "--images", "i", "--fonts", "-f", "--all"}

name = ""
flags = {}

def Help():
    print("This script will create a quick start for you to start programming webbsites and webb applications.")
    print("----------------------------------------------------------------------------------------------------")
    print("First argument should be the name of the project, which is mandatory")
    print("\t$ webbqs Name_Of_Your_Project")
    print("(Name should not include spaces)")
    print("----------------------------------------------------------------------------------------------------")
    print("Second argument should be any of theese flags:\n")
    print("--jquery\t-j\t- adds jquery to your project")
    print("--sass\t-s\t- adds sass to your project")
    print("--bootstrap\t-b\t- adds bootsrap to your project")
    print("--nodejs\t-n\t- adds node js to your project")
    print("--images\t-i\t- adds images folder to your project")
    print("--fonts\t-f\t- adds fonts folder to your project")
    print("--all\t- uses all of above")
    print("\t$ webbqs Name -i -j")
    print("(creates folder with html, jquery cdn, css, javascript and images folder)")
    print("If none of above is used there will be only html, css and javascript files created")

class Project:
    def __init__(self, name, flags):
        self.name = name
        self.flags = flags
    def Default(self):
        # HTML
        with open(self.name, "w") as f:
            f.write(html)
        # CSS
        os.mkdir("css")
        with open("css/style.css", "x") as f:
            pass
        # JavaScript
        os.mkdir("scripts")
        with open("scripts/script.js", "x") as f:
            pass
    def Create(self):
        self.Default()
        if "--jquery" in self.flags or "-j" in self.flags:
            with open("index.html", "r+") as f:
                lines = f.readlines()
                line_index = 0
                for line in lines:
                    if line.strip() == '<script src="scripts/script.js">':
                        break
                    line_index += 1
                lines.insert(line_index, jquery[0])
                f.writelines(lines)
        if "--sass" in self.flags or "-s" in self.flags:
            os.mkdir("scss")
            with open("scss/style.scss", "x") as f:
                pass
            with open("index.html", "r+") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip() != '<link src="css/style.css">':
                        f.write(line)
                    else:
                        f.write('\t<link src="scss/style.scss">')
        if "--bootstrap" in self.flags or "-b" in self.flags:
            with open("index.html" "r+") as f:
                lines = f.readlines()
                line_index = 0
                for line in lines:
                    if line.strip() == '<link src="css/style.css">' or line.strip() == '<link src="scss/style.scss">':
                        break
                    line_index += 1
                lines.insert(line_index, bootstrap[0])
                f.writelines(lines)
                for link in bootstrap:
                    lines = f.readlines()
                    if link != bootstrap[0]:
                        line_index = 0
                        for line in lines:
                            if line.strip() == '<script src="scripts/script.js">':
                                break
                            line_index += 1
                        lines.insert(line_index, link)
                        f.writelines(lines)
        if "--images" in self.flags or "-i" in self.flags:
            os.mkdir("images")
        if "--fonts" in self.flags or "-f" in self.flags:
            os.mkdir("fonts")


# Get input
try:
    name = sys.argv[1]
except:
    print("Please name your project")
    exit()
if len(sys.argv) > 2:
    for flag in flags:
        if flag not in available_flags:
            print("Please use available flags")
            print(available_flags)
            exit()
    flags = sys.argv[1:]
if "--all" in flags:
    flags = {"-j", "-b", "-s", "-i", "-f"}

# Create the project
dir_path = os.getcwd()+"/"+name
os.mkdir(dir_path)
os.chdir(dir_path)

project = Project(name, flags)
project.Create()
