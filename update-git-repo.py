#!/usr/bin/python

import sys
import os
import getopt
import datetime
import commands

debug=True


def debug_msg(message=None):
    if message and debug:
        print "DEBUG: " + message

class Update_tools(object):
    @staticmethod
    def cli_exception(type, value, tb):
        if not issubclass(type, KeyboardInterrupt):
            sys.__excepthook__(type, value, tb)

    def run(self):
        print "*******************************GAME START*********************************"
        if sys.stdin.isatty():
            sys.excepthook = Update_tools.cli_exception

        # get local dirs
        dirs = []
        cmd = 'ls -p | grep /'
        (status, dirs_str) = commands.getstatusoutput(cmd)
        debug_msg(dirs_str)
        if not status:
             dirs = (dirs_str.replace('/', '').split())

        debug_msg(str(dirs))

        # get current working directory
        current_patch = os.getcwd()
        debug_msg(current_patch)

        for dir in dirs:
            print "\n****************************************************"
            os.chdir(current_patch + "/" + dir)
            check_cmd = 'ls -ap | grep .git/'
            (dotgit_status, dotgit_dir) = commands.getstatusoutput(check_cmd)
            if dotgit_dir:
                print current_patch + "/" + dir
                os.system("git pull")
            else:
                debug_msg("dir %s is not git dir" % dir)

        # get subnet's id, use command 'neutron net-show ID  -F subnets -f value'
        #num = 0


        print "*******************************GAME OVER*********************************"

def main():
    update_tools = Update_tools()
    return update_tools.run()

if __name__ == "__main__":
    sys.exit(main())

