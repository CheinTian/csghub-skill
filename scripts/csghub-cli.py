#!/usr/bin/env python3
"""
CSGHub CLI - Command line interface for CSGHub API

Usage:
    export CSGHUB_TOKEN="your-api-token"
    export CSGHUB_URL="https://hub.opencsg-stg.com/api/v1"
    
    python csghub-cli.py <command> [args]

Commands:
    list models [query]          List all models
    list datasets [query]        List all datasets
    list codes [query]           List all codes
    list spaces [query]          List all spaces
    list mcps [query]            List all MCPs
    list my-models               List current user's models
    list my-datasets             List current user's datasets
    list my-spaces               List current user's spaces
    list my-mcps                 List current user's MCPs
    
    get model <namespace/name>   Get model details
    get dataset <namespace/name> Get dataset details
    get code <namespace/name>    Get code details
    get space <namespace/name>   Get space details
    get mcp <namespace/name>     Get MCP details
    get user <username>          Get user details
    
    files <type> <namespace/name> [path]  List files in repository
    download <type> <namespace/name> <file_path>  Download file
    
    inference list <model>       List inference endpoints
    inference create <model>     Create inference endpoint
    inference delete <model> <id>  Delete inference endpoint
    
    space status <namespace/name>  Get space status
    space logs <namespace/name>    Get space logs
    space stop <namespace/name>    Stop space
    space wakeup <namespace/name>  Wake up space
    
    finetune list <model>        List finetune jobs
    finetune logs <model> <id>   Get finetune logs
    
    balance [user_id]            Get credit balance
    bills <user_id> <start_date> <end_date>  List bills
    
    raw <method> <path> [body]   Make raw API request
"""

import os
import sys
import json
import argparse
from urllib.parse import urljoin
from datetime import datetime

try:
    import requests
except ImportError:
    print("Error: requests library required. Install with: pip install requests")
    sys.exit(1)


class CSGHubClient:
    """CSGHub API Client"""
    
    def __init__(self, base_url=None, token=None):
        self.base_url = base_url or os.environ.get('CSGHUB_URL', 'https://hub.opencsg-stg.com/api/v1')
        self.token = token or os.environ.get('CSGHUB_TOKEN')
        if not self.token:
            raise ValueError("API token required. Set CSGHUB_TOKEN environment variable.")
        
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': self.token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def request(self, method, path, **kwargs):
        """Make API request"""
        url = urljoin(self.base_url + '/', path.lstrip('/'))
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json() if response.text else None
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            if hasattr(e.response, 'text'):
                print(f"Response: {e.response.text}")
            sys.exit(1)
    
    def get(self, path, params=None):
        return self.request('GET', path, params=params)
    
    def post(self, path, json_data=None):
        return self.request('POST', path, json=json_data)
    
    def put(self, path, json_data=None):
        return self.request('PUT', path, json=json_data)
    
    def delete(self, path):
        return self.request('DELETE', path)
    
    # Resource listing
    def list_models(self, query=None, page=1, per=20):
        params = {'page': page, 'per': per}
        if query:
            params['search'] = query
        return self.get('/models', params)
    
    def list_datasets(self, query=None, page=1, per=20):
        params = {'page': page, 'per': per}
        if query:
            params['search'] = query
        return self.get('/datasets', params)
    
    def list_codes(self, query=None, page=1, per=20):
        params = {'page': page, 'per': per}
        if query:
            params['search'] = query
        return self.get('/codes', params)
    
    def list_spaces(self, query=None, page=1, per=20):
        params = {'page': page, 'per': per}
        if query:
            params['search'] = query
        return self.get('/spaces', params)
    
    def list_mcps(self, query=None, page=1, per=20):
        params = {'page': page, 'per': per}
        if query:
            params['search'] = query
        return self.get('/mcps', params)
    
    def list_user_models(self, username, page=1, per=20):
        return self.get(f'/user/{username}/models', {'page': page, 'per': per})
    
    def list_user_datasets(self, username, page=1, per=20):
        return self.get(f'/user/{username}/datasets', {'page': page, 'per': per})
    
    def list_user_spaces(self, username, page=1, per=20):
        return self.get(f'/user/{username}/spaces', {'page': page, 'per': per})
    
    def list_user_mcps(self, username, page=1, per=20):
        return self.get(f'/user/{username}/mcps', {'page': page, 'per': per})
    
    # Resource details
    def get_model(self, namespace, name):
        return self.get(f'/models/{namespace}/{name}')
    
    def get_dataset(self, namespace, name):
        return self.get(f'/datasets/{namespace}/{name}')
    
    def get_code(self, namespace, name):
        return self.get(f'/codes/{namespace}/{name}')
    
    def get_space(self, namespace, name):
        return self.get(f'/spaces/{namespace}/{name}')
    
    def get_mcp(self, namespace, name):
        return self.get(f'/mcps/{namespace}/{name}')
    
    def get_user(self, username):
        return self.get(f'/user/{username}')
    
    # File operations
    def list_files(self, repo_type, namespace, name, path=''):
        return self.get(f'/{repo_type}/{namespace}/{name}/tree', {'path': path})
    
    def get_blob(self, repo_type, namespace, name, file_path):
        return self.get(f'/{repo_type}/{namespace}/{name}/blob/{file_path}')
    
    def download_file(self, repo_type, namespace, name, file_path):
        return self.get(f'/{repo_type}/{namespace}/{name}/download/{file_path}')
    
    # Inference endpoints
    def list_inference(self, namespace, name):
        return self.get(f'/models/{namespace}/{name}/serverless')
    
    def create_inference(self, namespace, name, config=None):
        return self.post(f'/models/{namespace}/{name}/serverless', config)
    
    def delete_inference(self, namespace, name, endpoint_id):
        return self.delete(f'/models/{namespace}/{name}/serverless/{endpoint_id}')
    
    def get_inference_logs(self, namespace, name, endpoint_id, instance):
        return self.get(f'/models/{namespace}/{name}/serverless/{endpoint_id}/logs/{instance}')
    
    # Space operations
    def get_space_status(self, namespace, name):
        return self.get(f'/spaces/{namespace}/{name}/status')
    
    def get_space_logs(self, namespace, name):
        return self.get(f'/spaces/{namespace}/{name}/logs')
    
    def stop_space(self, namespace, name):
        return self.put(f'/spaces/{namespace}/{name}/stop')
    
    def wakeup_space(self, namespace, name):
        return self.put(f'/spaces/{namespace}/{name}/wakeup')
    
    # Finetune operations
    def list_finetune(self, namespace, name):
        return self.get(f'/models/{namespace}/{name}/finetune')
    
    def get_finetune_logs(self, namespace, name, job_id, instance):
        return self.get(f'/models/{namespace}/{name}/finetune/{job_id}/logs/{instance}')
    
    # Accounting
    def get_balance(self, user_id):
        return self.get(f'/accounting/credit/{user_id}/balance')
    
    def list_bills(self, user_id, start_date, end_date, scene=10):
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'scene': scene,
            'instance_name': 'default'
        }
        return self.get(f'/accounting/credit/{user_id}/bills', params)
    
    def list_statements(self, user_id, start_time, end_time, scene=10, instance_name='default'):
        params = {
            'start_time': start_time,
            'end_time': end_time,
            'scene': scene,
            'instance_name': instance_name
        }
        return self.get(f'/accounting/credit/{user_id}/statements', params)


def print_json(data):
    """Pretty print JSON"""
    print(json.dumps(data, indent=2, ensure_ascii=False))


def print_table(headers, rows):
    """Print data as table"""
    if not rows:
        print("No data")
        return
    
    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Print header
    header_line = " | ".join(h.ljust(w) for h, w in zip(headers, widths))
    print(header_line)
    print("-" * len(header_line))
    
    # Print rows
    for row in rows:
        print(" | ".join(str(cell).ljust(w) for cell, w in zip(row, widths)))


def parse_namespace_name(full_name):
    """Parse namespace/name format"""
    parts = full_name.split('/')
    if len(parts) != 2:
        raise ValueError(f"Invalid format: {full_name}. Use: namespace/name")
    return parts[0], parts[1]


def cmd_list(client, args):
    """Handle list commands"""
    resource = args.resource
    query = args.query if hasattr(args, 'query') else None
    
    if resource == 'models':
        data = client.list_models(query=query)
    elif resource == 'datasets':
        data = client.list_datasets(query=query)
    elif resource == 'codes':
        data = client.list_codes(query=query)
    elif resource == 'spaces':
        data = client.list_spaces(query=query)
    elif resource == 'mcps':
        data = client.list_mcps(query=query)
    elif resource == 'my-models':
        # Get current user first
        # This is a simplification - you'd need to get current user from token
        print("Note: Using 'me' as username. Provide username if different.")
        data = client.list_user_models('me')
    elif resource == 'my-datasets':
        data = client.list_user_datasets('me')
    elif resource == 'my-spaces':
        data = client.list_user_spaces('me')
    elif resource == 'my-mcps':
        data = client.list_user_mcps('me')
    else:
        print(f"Unknown resource: {resource}")
        return
    
    # Extract data from response
    if isinstance(data, dict) and 'data' in data:
        items = data['data']
    else:
        items = data
    
    if not items:
        print("No items found")
        return
    
    # Print as table if possible
    if isinstance(items, list) and len(items) > 0:
        if isinstance(items[0], dict):
            # Determine columns based on resource type
            if resource in ['models', 'my-models']:
                headers = ['Name', 'Description', 'Downloads', 'Updated']
                rows = []
                for item in items:
                    name = f"{item.get('namespace', '')}/{item.get('name', '')}"
                    desc = item.get('description', '')[:50] if item.get('description') else ''
                    downloads = item.get('download_count', 0)
                    updated = item.get('updated_at', '')[:10] if item.get('updated_at') else ''
                    rows.append([name, desc, downloads, updated])
                print_table(headers, rows)
            elif resource in ['datasets', 'my-datasets']:
                headers = ['Name', 'Description', 'Downloads', 'Updated']
                rows = []
                for item in items:
                    name = f"{item.get('namespace', '')}/{item.get('name', '')}"
                    desc = item.get('description', '')[:50] if item.get('description') else ''
                    downloads = item.get('download_count', 0)
                    updated = item.get('updated_at', '')[:10] if item.get('updated_at') else ''
                    rows.append([name, desc, downloads, updated])
                print_table(headers, rows)
            elif resource in ['spaces', 'my-spaces']:
                headers = ['Name', 'Description', 'Status', 'Updated']
                rows = []
                for item in items:
                    name = f"{item.get('namespace', '')}/{item.get('name', '')}"
                    desc = item.get('description', '')[:50] if item.get('description') else ''
                    status = item.get('status', '')
                    updated = item.get('updated_at', '')[:10] if item.get('updated_at') else ''
                    rows.append([name, desc, status, updated])
                print_table(headers, rows)
            else:
                print_json(items)
        else:
            print_json(items)
    else:
        print_json(items)


def cmd_get(client, args):
    """Handle get commands"""
    resource = args.resource
    identifier = args.identifier
    
    try:
        if resource == 'model':
            ns, name = parse_namespace_name(identifier)
            data = client.get_model(ns, name)
        elif resource == 'dataset':
            ns, name = parse_namespace_name(identifier)
            data = client.get_dataset(ns, name)
        elif resource == 'code':
            ns, name = parse_namespace_name(identifier)
            data = client.get_code(ns, name)
        elif resource == 'space':
            ns, name = parse_namespace_name(identifier)
            data = client.get_space(ns, name)
        elif resource == 'mcp':
            ns, name = parse_namespace_name(identifier)
            data = client.get_mcp(ns, name)
        elif resource == 'user':
            data = client.get_user(identifier)
        else:
            print(f"Unknown resource: {resource}")
            return
        
        print_json(data)
    except ValueError as e:
        print(f"Error: {e}")


def cmd_files(client, args):
    """Handle files command"""
    repo_type = args.type
    full_name = args.name
    path = args.path if hasattr(args, 'path') else ''
    
    try:
        ns, name = parse_namespace_name(full_name)
        data = client.list_files(repo_type, ns, name, path)
        
        if isinstance(data, dict) and 'data' in data:
            files = data['data']
        else:
            files = data
        
        if isinstance(files, list):
            headers = ['Type', 'Name', 'Size', 'Path']
            rows = []
            for f in files:
                ftype = 'dir' if f.get('type') == 'dir' else 'file'
                fname = f.get('name', '')
                fsize = f.get('size', '')
                fpath = f.get('path', '')
                rows.append([ftype, fname, fsize, fpath])
            print_table(headers, rows)
        else:
            print_json(files)
    except ValueError as e:
        print(f"Error: {e}")


def cmd_inference(client, args):
    """Handle inference commands"""
    action = args.action
    
    try:
        if action == 'list':
            ns, name = parse_namespace_name(args.model)
            data = client.list_inference(ns, name)
            print_json(data)
        elif action == 'create':
            ns, name = parse_namespace_name(args.model)
            config = None
            if args.config:
                config = json.loads(args.config)
            data = client.create_inference(ns, name, config)
            print_json(data)
        elif action == 'delete':
            ns, name = parse_namespace_name(args.model)
            data = client.delete_inference(ns, name, args.id)
            print_json(data)
        elif action == 'logs':
            ns, name = parse_namespace_name(args.model)
            data = client.get_inference_logs(ns, name, args.id, args.instance)
            print_json(data)
    except ValueError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON config: {e}")


def cmd_space(client, args):
    """Handle space commands"""
    action = args.action
    
    try:
        ns, name = parse_namespace_name(args.name)
        
        if action == 'status':
            data = client.get_space_status(ns, name)
        elif action == 'logs':
            data = client.get_space_logs(ns, name)
        elif action == 'stop':
            data = client.stop_space(ns, name)
        elif action == 'wakeup':
            data = client.wakeup_space(ns, name)
        else:
            print(f"Unknown action: {action}")
            return
        
        print_json(data)
    except ValueError as e:
        print(f"Error: {e}")


def cmd_finetune(client, args):
    """Handle finetune commands"""
    action = args.action
    
    try:
        if action == 'list':
            ns, name = parse_namespace_name(args.model)
            data = client.list_finetune(ns, name)
            print_json(data)
        elif action == 'logs':
            ns, name = parse_namespace_name(args.model)
            data = client.get_finetune_logs(ns, name, args.id, args.instance)
            print_json(data)
    except ValueError as e:
        print(f"Error: {e}")


def cmd_accounting(client, args):
    """Handle accounting commands"""
    action = args.action
    
    if action == 'balance':
        user_id = args.user_id if hasattr(args, 'user_id') else 'current'
        data = client.get_balance(user_id)
        print_json(data)
    elif action == 'bills':
        data = client.list_bills(args.user_id, args.start_date, args.end_date)
        print_json(data)
    elif action == 'statements':
        data = client.list_statements(args.user_id, args.start_time, args.end_time)
        print_json(data)


def cmd_raw(client, args):
    """Handle raw API requests"""
    method = args.method.upper()
    path = args.path
    
    if args.body:
        try:
            body = json.loads(args.body)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON body: {e}")
            return
    else:
        body = None
    
    if method == 'GET':
        data = client.get(path)
    elif method == 'POST':
        data = client.post(path, body)
    elif method == 'PUT':
        data = client.put(path, body)
    elif method == 'DELETE':
        data = client.delete(path)
    else:
        print(f"Unsupported method: {method}")
        return
    
    print_json(data)


def main():
    parser = argparse.ArgumentParser(
        description='CSGHub CLI - Interact with CSGHub API',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Environment Variables:
  CSGHUB_TOKEN    API authentication token (required)
  CSGHUB_URL      Base API URL (default: https://hub.opencsg-stg.com/api/v1)

Examples:
  export CSGHUB_TOKEN="your-token"
  
  # List models
  python csghub-cli.py list models
  
  # Get model details
  python csghub-cli.py get model org/model-name
  
  # List files in a model
  python csghub-cli.py files models org/model-name
  
  # Get space status
  python csghub-cli.py space status org/space-name
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List resources')
    list_parser.add_argument('resource', choices=[
        'models', 'datasets', 'codes', 'spaces', 'mcps',
        'my-models', 'my-datasets', 'my-spaces', 'my-mcps'
    ])
    list_parser.add_argument('query', nargs='?', help='Search query')
    
    # Get command
    get_parser = subparsers.add_parser('get', help='Get resource details')
    get_parser.add_argument('resource', choices=['model', 'dataset', 'code', 'space', 'mcp', 'user'])
    get_parser.add_argument('identifier', help='Resource identifier (namespace/name or username)')
    
    # Files command
    files_parser = subparsers.add_parser('files', help='List files in repository')
    files_parser.add_argument('type', choices=['models', 'datasets', 'codes', 'spaces', 'mcps'])
    files_parser.add_argument('name', help='Repository name (namespace/name)')
    files_parser.add_argument('path', nargs='?', default='', help='Directory path')
    
    # Inference command
    inference_parser = subparsers.add_parser('inference', help='Manage model inference endpoints')
    inference_parser.add_argument('action', choices=['list', 'create', 'delete', 'logs'])
    inference_parser.add_argument('model', help='Model name (namespace/name)')
    inference_parser.add_argument('--id', help='Inference endpoint ID')
    inference_parser.add_argument('--instance', help='Instance name')
    inference_parser.add_argument('--config', help='JSON configuration for create')
    
    # Space command
    space_parser = subparsers.add_parser('space', help='Manage spaces')
    space_parser.add_argument('action', choices=['status', 'logs', 'stop', 'wakeup'])
    space_parser.add_argument('name', help='Space name (namespace/name)')
    
    # Finetune command
    finetune_parser = subparsers.add_parser('finetune', help='Manage finetune jobs')
    finetune_parser.add_argument('action', choices=['list', 'logs'])
    finetune_parser.add_argument('model', help='Model name (namespace/name)')
    finetune_parser.add_argument('--id', help='Job ID')
    finetune_parser.add_argument('--instance', help='Instance name')
    
    # Accounting command
    accounting_parser = subparsers.add_parser('accounting', help='Accounting operations')
    accounting_parser.add_argument('action', choices=['balance', 'bills', 'statements'])
    accounting_parser.add_argument('--user-id', default='current', help='User ID')
    accounting_parser.add_argument('--start-date', help='Start date (YYYY-MM-DD)')
    accounting_parser.add_argument('--end-date', help='End date (YYYY-MM-DD)')
    accounting_parser.add_argument('--start-time', help='Start time (YYYY-MM-DD HH:MM:SS)')
    accounting_parser.add_argument('--end-time', help='End time (YYYY-MM-DD HH:MM:SS)')
    
    # Raw command
    raw_parser = subparsers.add_parser('raw', help='Make raw API request')
    raw_parser.add_argument('method', choices=['GET', 'POST', 'PUT', 'DELETE'])
    raw_parser.add_argument('path', help='API path')
    raw_parser.add_argument('body', nargs='?', help='JSON body')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        client = CSGHubClient()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    # Dispatch to appropriate handler
    handlers = {
        'list': cmd_list,
        'get': cmd_get,
        'files': cmd_files,
        'inference': cmd_inference,
        'space': cmd_space,
        'finetune': cmd_finetune,
        'accounting': cmd_accounting,
        'raw': cmd_raw,
    }
    
    handler = handlers.get(args.command)
    if handler:
        handler(client, args)
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()


if __name__ == '__main__':
    main()
