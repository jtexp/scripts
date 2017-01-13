#!/usr/bin/python3

import os
import re
import subprocess

rootdir = "/home/john/Downloads/bnra"
proj = "CriminalIntent"

def dir_loop():
    for subdir, dirs, files in os.walk(rootdir):
        for d in dirs:
            print(os.path.join(subdir, d))

def get_subd():
    out = []
    for subdir in os.listdir(rootdir):
        if os.path.isdir(subdir):
            out.append(subdir)
    return out

def get_sd(d):
    return [subdir for subdir in os.listdir(d) if os.path.isdir(subdir)]

def contains_ci(d):
    d2 = os.path.join(rootdir, d)
    if proj in os.listdir(d2):
        return True
    else:
        return False



def filter_r(s):
    p = re.compile('\d\d_*')
    return p.match(s)



def main():

    dir_loop()
    print("----------")
    get_subd()
    l = get_sd(rootdir)
    l = sorted(list(filter(filter_r, l)))
    # l is a list of directories, now find the ones that include criminal intent
    l2 = []
    for i in l:
        if contains_ci(i):
            l2.append(i)
    print(l2)
    repo = os.path.join(rootdir, proj)
    subprocess.call(["git", "init", "repo"])
    git_ignore = os.path.join(rootdir, ".gitignore")
    subprocess.call(["cp", git_ignore, rootdir])
    repo = os.path.join(rootdir, proj, ".git")
    git_ignore = os.path.join(rootdir, proj, ".gitignore")
    for i in l2:
        path = os.path.join(rootdir, i, "CriminalIntent")
        print(path)

        cmd = "mv {} {}".format(repo, path)
        subprocess.call(cmd.split())
        cmd = "mv {} {}".format(git_ignore, path)
        subprocess.call(cmd.split())
        os.chdir(path)
        subprocess.call(["git", "add", "--all"])
        subprocess.call(["git", "commit", "-m", i])
        repo = os.path.join(path, ".git")
        git_ignore = os.path.join(path, ".gitignore")


if __name__ == "__main__": 
    main()    
