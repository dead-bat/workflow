"""
WORKFLOW ENGINE
ver 0.1a

A simple workflow automation solution

BY ROBBY EMSLIE

USAGE

$ python workflow.py [ "WORKFLOW NAME" | <workflow_id> ]

"WORKFLOW NAME" is a quoted string matching the human-readable name of the workflow. Alternatively,
you may provided <workflow_id> as an integer preceeded by an underscore (ex., "_123") matching the
workflow's ID in globalconfig.


"""

from globalconfig import CONFIG
from libs.main import Workflow
import sys, json, yaml, requests, time

## DEFINITIONS

def export_log(workflow_name, job_id, log_data):
    log_dir = CONFIG['dirs']['logs']
    out_file = f"{workflow_name}_{job_id}.json"
    log_string = json.dumps(log_data, indent=4)
    with open(f"{log_dir}/{out_file}", "w") as of:
        of.write(log_string)
    return out_file

def get_workflow(workflow):
    selected_workflow = {
        'name': None,
        'id': None,
        'dir': None
    }
    all_workflows = CONFIG['workflows']
    if workflow[0] == "_":
        match_field = 'id'
        match_val = int(workflow[1:])
    else:
        match_field = 'name'
        match_val = workflow
    for flow in all_workflows:
        if flow[match_field] == match_val:
            selected_workflow = {
                'name': flow['name'],
                'id': flow['id'],
                'dir': flow['dir']
            }
    if selected_workflow['dir'] is None:
        raise Exception("Workflow not found")
    return selected_workflow

def execute_workflow(workflow):
    working_dir = workflow['dir']
    workflow_file = f"{working_dir}/start.yaml"
    workflow = Workflow(yaml.load_all(workflow_file), f"{str(time.time()).split('.')[0]}", working_dir)
    while workflow.error_state is False:
        workflow.initialize()
        workflow.execute()
        workflow.cleanup()
    if workflow.error_state is True or workflow.status == 'failed':
        print("Something went wrong. Please review job logs...")
    return workflow

## EXECUTION

def main(workflow):
    workflow_file = get_workflow(workflow)
    workflow_job = execute_workflow(workflow_file)
    log = export_log(workflow_file['name'], workflow_job.job_id, workflow_job.log)
    print(f"Workflow exited with status '{workflow_job.status}'.")

main(sys.argv[1])