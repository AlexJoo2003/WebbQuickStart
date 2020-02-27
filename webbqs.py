import sys
import os


try:
    name = sys.argv[1]
except:
    print("Please name your project")
    exit()

html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
    *Bootstrap CSS
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    


*Bootstrap JS
*Jquery JS
<script src="scripts/script.js"></script>
</body>
</html>
'''

jquery = ['''$(document).ready(function(){

});''',
    '<script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>\n'
]

bootstrapCSS = '\t<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">\n'
bootstrapJS = [
    '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>\n',
    '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>\n',
    '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>\n'
]

available_flags = ["-j", "-b", "-s", "-i", "-f", "--all"]


class Project:
    def __init__(self, name, flags):
        self.name = name
        self.flags = flags

    def Create(self):
        os.mkdir("css")
        os.mkdir("scripts")
        with open("index.html", "w") as f:
            f.write(html)
        f = open("css/style.css", "x").close()
        f = open("scripts/script.js", "x").close()

        if "-j" in self.flags:
            # HTML JQuery CDN
            with open("index.html", "r") as f:
                lines = f.readlines()
            with open("index.html", "w") as f:
                for line in lines:
                    if line.strip() == "*Jquery JS":
                        f.write(jquery[1])
                    else:
                        f.write(line)
            # JQuery Quick start
            with open("scripts/script.js", "w") as f:
                f.write(jquery[0])
        
        if "-b" in self.flags:
            # HTML Bootstrap CDN CSS
            with open("index.html", "r") as f:
                lines = f.readlines()
            with open("index.html", "w") as f:
                for line in lines:
                    if line.strip() == "*Bootstrap CSS":
                        f.write(bootstrapCSS)
                    else:
                        f.write(line)
            # HTML Bootstrap CDN JS
            with open("index.html", "r") as f:
                lines = f.readlines()
            with open("index.html", "w") as f:
                for line in lines:
                    if line.strip() == "*Bootstrap JS":
                        for link in bootstrapJS:
                            f.write(link)
                    else:
                        f.write(line)

        if "-s" in self.flags:
            # Add Sass file
            os.mkdir("sass")
            f = open("sass/style.scss", "x").close()
        
        if "-i":
            os.mkdir("images")

        if "-f":
            os.mkdir("fonts")
        
        # Remove all the placeholders
        # with open("index.html", "r") as f:
        #     lines = f.readline()
        # with open("index.html", "w") as f:
        #     for line in lines:
        #         if '*' in line:
        #             f.write(line)


if len(sys.argv) > 2:
    flags = sys.argv[2:]
    for flag in flags:
        if flag not in available_flags:
            print("Please use only these flags:")
            print(available_flags)
            exit()

dir_path = os.getcwd()+"/"+name
os.mkdir(dir_path)
os.chdir(dir_path)

project = Project(name, flags)
project.Create()
