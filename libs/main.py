"""
WORKFLOW ENGINE
main.py

This is the workflow engine, itself, which is actually runs the workflows based on
the specifications found in the <project_folder>/start.yaml file.

"""

from globalconfig import CONFIG
import yaml, requests, json, time, tempfile
from datetime import datetime as dt

## GENERAL FUNCTIONS

## CLASSES

class Workflow:
    def __init__(self, workflow, job_id, working_dir):
        self.spec = workflow
        self.job_id = job_id
        self.host_directory = working_dir
        self.log = [{f"{dt.now().strftime('%Y-%m-%dT%H:%M:%S')}": {'message': "New workflow instance initialized."}}]
        self.error_state = False
        self.status = None
    def initialize(self):
        message, error, status = None, False, None
        return message, error, status
    def execute(self):
        message, error, status = None, False, None
        return message, error, status
    def cleanup(self):
        message, error, status = None, False, None
        return message, error, status