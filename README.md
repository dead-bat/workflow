# workflow
A simple workflow automation solution

## Directory Scheme

- `workflow/` is the root directory where Workflow lives
    - `globalconfig.ini` contains the broad, general configuration of Workflow
    - `workflow.py` is the Workflow engine, itself
    - `workflow_util.py` is the Workflow utility that can be used for various administrative tasks for the Workflow engine
    - `libs/` contains the supporting libraries for the Workflow engine
        - `...`
    - `apps/` contains the application modules that allow the Workflow engine to connecto various third-party resources
        - `app_01.py` is an application module for a single application
        - `app_02.py` is another application module for a second application
    - `projects/` contains automation solutions, silo'ed in folders to keep them together as packages
        - `automation_01/`
            - `start.json` is the root automation specification, and is the only **required** file for an automation.
            - `workflow_01.json` is an additional workflow specification -- perhaps a subtask
            - `workflow_02.json` is another workflow specification, perhaps a second stage or an alternative pipeline
            - `assets/` contains additional supporting artifacts for the project -- such as a TinyDB instance, a list of properties that can be referenced across all the workflows, and templates for messages and reports.
                - `tinydb`
                - `properties.json`
                - `templates/`
                    - `message_template_01.html`
                    - `report_template_01.html`
            - `connections/` contains account configurations for establishing instances of a connection to a third-party application
                - `app_01_conn_01.json` contains connection configuration for a connection to the app_01 application
                - `app_02_conn_01.json` contains a connection configuration for app_02
        - `automation_02/`
            - `start.json`
            - `assets/` is empty for this project
            - `connections/`
                - `app_01_conn_02.json` contains an additional connection configuration for app_01 application
                