"""
Workato Embedded App for Workflow Engine
"""
import requests, json

app = {
    'meta': {
        'name': 'Workato Embedded',
        'description': 'Tools for automating with the Workato Embedded API'
    },
    'connection': {
        'type': 'bearer_token',
        'config': [
            { 'name': 'api_token', 'type': 'str' },
            { 'name': 'root_url', 'type': 'str' }
        ],
        'establish': lambda config: {
            'host': config['root_url'],
            'header': {'Authorization': f"Bearer {config['api_token']}"}
        },
        'refresh_on': [],
        'refresh': {},
        'test': {}
    },
    'methods': {
        #
    },
    'actions': {
        #
    },
    'triggers': {
        #
    },
    'options': {
        #
    }
}