# snippets
a collection of useful and useless code snippets

## print random string
```bash
< /dev/urandom tr -dc A-Za-z0-9 | head -c${1:-64};echo;
# if the above fails:
openssl rand -base64 64 | tr -dc _A-Z-a-z-0-9 && echo "" # may be less than 64 chars
```

## delete dead merged git branches
```bash
git fetch --all
git up
for i in `git branch -a | grep remote | grep -v HEAD`; do git branch --track ${i#remotes/origin/} $i; done

git checkout master
echo "the following branches have been merged into the master branch and will be purged from your local machine and from the remote:"
git branch --merged | grep -v "\*" | grep -v "master" | grep -v "develop" | xargs -n 1

while true; do
read -p "Do you want to proceed? (y/n): " yn
case $yn in
        [Yy]* ) break;;
        [Nn]* ) echo "* You canceled; "; exit;;
        * ) echo "| Please type (Y/N): ";;
esac
done

git branch --merged | grep -v "\*" | grep -v "master" | grep -v "develop" | xargs -n 1 git push --delete origin
git branch --merged | grep -v "\*" | grep -v "master" | grep -v "develop" | xargs -n 1 git branch -d
```

## search for all files with name "pattern" in current working directory 

```
find . -name "pattern"
```

```python
#!/usr/bin/python
def get_file_names(filename_expression, start_path="."):
    matches = []
    for root, dirnames, filenames in os.walk(start_path):
        for filename in fnmatch.filter(filenames, filename_expression):
                matches.append(os.path.join(root, filename))
    return matches
```

## replace strings in text file
```python
#!/usr/bin/python
def replaceValue(file, old, new):
    newlines = []
    with open(file,'r') as f:
        for line in f.readlines():
            newlines.append(line.replace(old, new))

    with open(file, 'w') as f:
        for line in newlines:
            f.write(line)
```            
## yes/no prompt

```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")    
```

# mac specific things

[mac-specific](mac-specific.md)

