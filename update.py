import os
from subprocess import run as srun from os import path as ospath from sys import executable from os import execl as osexecl import sys
import sys
from subprocess import run as srun
 
 
UPSTREAM_REPO = 'https://github.com/harsha7668/metabor'
UPSTREAM_REPO = 'https://github.com/harsha7668/metabor' UPSTREAM_BRANCH = 'SH24BOTS-GD-REVERSION-GRP'
UPSTREAM_BRANCH = 'SH24BOTS-GD-REVERSION-GRP'
 
 
if UPSTREAM_REPO:
if UPSTREAM_REPO is not None: if ospath.exists('.git'): srun(["rm", "-rf", ".git"])
    if os.path.exists('.git'):
        srun(["rm", "-rf", ".git"])
 
 
    update = srun(f"""
update = srun([f"git init -q \
        git init -q &&
                 && git config --global user.email sunriseseditsoffical249@gmail.com \
        git config --global user.email "sunriseseditsoffical249@gmail.com" &&
                 && git config --global user.name metamorpher \
        git config --global user.name "metamorpher" &&
                 && git add . \
        git add . &&
                 && git commit -sm update -q \
        git commit -sm "update" -q &&
                 && git remote add origin {UPSTREAM_REPO} \
        git remote add origin {UPSTREAM_REPO} &&
                 && git fetch origin -q \
        git fetch origin -q &&
                 && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)
        git reset --hard origin/{UPSTREAM_BRANCH} -q
    """, shell=True)
 
 
    if update.returncode == 0:

        print("Update successful. Restarting bot...")
if update.returncode == 0:
        bot_path = os.path.join(os.getcwd(), "bot.py")  # Ensure correct path
    osexecl(sys.executable, sys.executable, "bot.py")
        if os.path.exists(bot_path):
else:
            os.execl(sys.executable, sys.executable, bot_path)
    print('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
        else:

            print(f"Error: {bot_path} not found. Cannot restart.")
osexecl(executable, executable, "bot.py")
            sys.exit(1)
    else:
        print("Something went wrong while updating, check UPSTREAM_REPO if valid or not!")
        sys.exit(1)
