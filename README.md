# snippets
a collection of useful and useless code snippets

print random string
```
< /dev/urandom tr -dc A-Za-z0-9 | head -c${1:-64};echo;
```

delete dead merged git branches
```
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
