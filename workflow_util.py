"""
    WORKFLOW_UTIL
    The Workflow Engine Administrative Utility

    SAMPLE

    $ python workflow_util.py <operation> <parameters>

"""

import sys, os, json
from globalconfig import CONFIG

configfile = 'globalconfig.py'
CFG = CONFIG

## DEFINITIONS

def createWorkflowSuite(name):
    status = {
        'error': False,
        'message': "Creating new project"
    }
    new_project_folder = "_".join(name.split(" "))
    try:
        new_project_root = f"{CFG['dirs']['proj']}/{new_project_folder}"
        os.mkdir(new_project_root)
        os.mkdir(f"{new_project_root}/connections")
        os.mkdir(f"{new_project_root}/assets")
        status['message'] = f"New project created succesfully at {new_project_root}"
    except:
        print("Cannot create directories for project...")
        status['error'] = True
    if status['error'] is False:
        try:
            id = CFG['workflows'][len(CFG['workflows']) - 1]['id'] + 1
            CFG['workflows'].append({'id': id, 'name': name, 'dir': new_project_folder})
            cfg_string = json.dumps(CFG, indent=4)
            with open(configfile, 'w') as cf:
                cf.write(f"CONFIG = {cfg_string}")
        except:
            print("Could not update config file. Manual update rquired.")
            status['error'] = True
            status['message'] = "Project folders created. Could not update config file; it will need to be manually updaed."
    return status

## EXECUTABLES

def main(params):
    if params[0] == 'NEW':
        try:
            createWorkflowSuite(params[1])
        except IndexError:
            print("Missing new project name. Please try again.")
        except:
            print("Something went wrong...")

main(sys.argv[1:])