from os import mkdir
from shutil import copy2
from shutil import rmtree
from zipfile import ZipFile
def copy(original, new):
    copy2(f'./make/{original}', f'{project}/{new}')
def changeline(path, line, content):
    with open(path, 'r') as file:
        lines = file.readlines()
        if 1 <= line <= len(lines):
            lines[line - 1] = content + '\n'
            with open(path, 'w') as file:
                file.writelines(lines)
            with open(path, "r") as file:
                new_file = file.read()
    return new_file

project = input("Project Name: ")

while not all(char in "abcdefghijklmnopqrstuv1234567890-" for char in project):
    print("All lowercase & No spaces! Dashes are includes.")
    project = input("Project Name: ")

# Make Directories
try:
    mkdir(f"{project}")
except:
    print()
try:    
    mkdir(f"{project}/public")
except:
    print()
try:
    mkdir(f"{project}/src")
except:
    print()
try:
    mkdir(f"{project}/src/app")
except:
    print()
try:
    mkdir(f"{project}/src/styles")
except:
    print()
    
with ZipFile('make.zip', 'r') as zip_ref:
    zip_ref.extractall('')

copy('tsconfig.json', '')
copy('prettier.config.js', '')
copy('postcss.config.js', '')
copy('next.config.js', '')
copy('next-env.d.ts', '')
copy('eslint.config.js', '')
copy('src/env.js', 'src/')
copy('src/app/layout.tsx', 'src/app/')
copy('src/app/page.tsx', 'src/app/')
copy('src/styles/globals.css', 'src/styles/')
copy('public/favicon.ico', 'public/')
with open(f'{project}/package.json', 'w') as file:
    file.write(changeline('./make/package.json', 2, f'  "name": "{project}",'))
rmtree('make')

