from subprocess import run as srun
from os import path as ospath
from sys import executable
from os import execl as osexecl
import sys

UPSTREAM_REPO = 'https://github.com/harsha7668/metabor'
UPSTREAM_BRANCH = 'SH24BOTS-GD-REVERSION-GRP'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update = srun(f"""
        git init -q &&
        git config --global user.email "sunriseseditsoffical249@gmail.com" &&
        git config --global user.name "metamorpher" &&
        git add . &&
        git commit -sm "update" -q &&
        git remote add origin {UPSTREAM_REPO} &&
        git fetch origin -q &&
        git reset --hard origin/{UPSTREAM_BRANCH} -q
    """, shell=True)

    if update.returncode == 0:
        print("Update successful. Restarting bot...")
        bot_path = ospath.join(ospath.dirname(__file__), "bot.py")  # Ensure correct path
        if ospath.exists(bot_path):
            osexecl(executable, executable, bot_path)
        else:
            print(f"Error: {bot_path} not found. Cannot restart.")
            sys.exit(1)
    else:
        print("Something went wrong while updating, check UPSTREAM_REPO if valid or not!")
        sys.exit(1)
