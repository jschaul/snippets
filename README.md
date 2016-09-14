# snippets
a collection of useful and useless code snippets

Table of Contents
=================

  * [snippets](#snippets)
    * [print random string](#print-random-string)
    * [prettify json output](#prettify-json-output)
    * [delete dead merged git branches](#delete-dead-merged-git-branches)
    * [search for all files with name "pattern" in current working directory](#search-for-all-files-with-name-pattern-in-current-working-directory)
    * [replace strings in text file](#replace-strings-in-text-file)
    * [yes/no prompt](#yesno-prompt)
    * [find files containing keywordA](#find-files-containing-keyworda)
    * [tcp dump](#tcp-dump)
    * [jvm java memory leak heap analysis on running server](#jvm-java-memory-leak-heap-analysis-on-running-server)
    * [profile things in python](#profile-things-in-python)
    * [python build/environment best practices](#python-buildenvironment-best-practices)
    * [list all crontabs for all users](#list-all-crontabs-for-all-users)
  * [mac specific things](#mac-specific-things)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)


## print random string
```bash
< /dev/urandom tr -dc A-Za-z0-9 | head -c${1:-64};echo;
# if the above fails:
openssl rand -base64 64 | tr -dc _A-Z-a-z-0-9 && echo "" # may be less than 64 chars
```

## prettify json output
```bash
cat file.json | python -m json.tool
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

## find files containing keywordA

place files in text file
```
grep -Rl keywordA > keywordA.txt
```
search for lines with keywordsB and C in those files:
```
grep "keyword B" -- `cat keywordA.txt` | grep keywordC
```

## tcp dump

see stuff on udp port 514 (e.g. rsyslogd)

```bash
# execute as root user
tcpdump -i lo udp port 514 -A  
```

## jvm java memory leak heap analysis on running server

get java heap histogram
```
jmap -histo:live <process_id> > file.txt
```

full dump
```
jmap -dump:format=b,file=dump.hprof  <process_id>
```

if oracle java: e.g. force garbage collection, see
```
jcmd <process_id> help
```

## profile things in python

see [https://docs.python.org/2/library/profile.html](https://docs.python.org/2/library/profile.html)

## python build/environment best practices

see [https://moshez.wordpress.com/2016/01/27/learning-python-the-ecosystem/](this)

## list all crontabs for all users

```
for user in $(cut -f1 -d: /etc/passwd); do echo "crons for $user:"; crontab -u $user -l 2>/dev/null | grep -v '^#'; done
```
(http://stackoverflow.com/questions/134906/how-do-i-list-all-cron-jobs-for-all-users)


## bump chef cookbook metadata.rb file

(code taken from: http://blog.backslasher.net/cookbook-versioning.html)

```
#!/usr/bin/env ruby

target_branch='master'
has_minor=`git log #{target_branch}.. --grep=BUMP_MINOR`.length > 0
has_major=`git log #{target_branch}.. --grep=BUMP_MAJOR`.length > 0
bump_type=if has_major then 'major'
          elsif has_minor then 'minor'
          else 'build'
          end

# Get next version
split_options=['major','minor','build']
split_index=split_options.index(bump_type)
raise 'unknown bump modifier' if split_index.nil?
metadata_file='./metadata.rb'
metadata=File.read(metadata_file)
version_line=metadata.split("\n").select{|s|s[/^\s*version\W/]}.last
version_regex=/("|')([\d\.]+)("|')/
version=version_line[version_regex,2]
v_arr=version.split('.')
v_arr[split_index]=(v_arr[split_index].to_i+1).to_s
(split_index+1..v_arr.length-1).each{|a|v_arr[a]=0} # Zero other cells
new_version=v_arr.join('.')

# Read file
metadata_file='./metadata.rb'
metadata=File.read(metadata_file)

# Find version line
version_regex=/("|')([\d\.]+)("|')/
version_line=metadata.split("\n").select{|s|s[/^\s*version\W/]}.last

# Generate new one
new_version_line=version_line.gsub(version_regex,"'#{new_version}'")
new_metadata=metadata.gsub("\n#{version_line}\n","\n#{new_version_line}\n")

# Write back to file
File.write(metadata_file,new_metadata)
```

# ~/.gitconfig alias

```
[alias]
        lg = log --graph --decorate --pretty=format:'%C(blue)%h%Creset -%C(red)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative
```

(taken from https://github.com/wmalik/dotfiles)

# mac specific things

[mac-specific](mac-specific.md)

