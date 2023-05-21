from typing import List
from flask import Flask, jsonify, Response
import route_methods as route


class EndpointAction:

    def __init__(self, action, mimetype):
        self.action = action
        self.response = Response(status=200, headers={}, mimetype=mimetype)

    def __call__(self, *args, **kwargs):
        res = self.action()

        if self.response.mimetype == 'application/json':
            self.response = jsonify(res)
            return self.response

        elif self.response.mimetype == 'text/plain':
            return self.response

        else:
            raise NotImplementedError('Returned Response type not implemented')


class MyWebApp:
    app = None

    def __init__(self, appName=None):
        if appName is None:
            import pathlib
            appName = pathlib.Path(__file__)
        self.app = Flask(appName)

    def add_route(self, route_str_path, route_name, route_method, mimetype, options: List[str] = None) -> None:
        if options is None:
            options = ['GET']
        self.app.add_url_rule(route_str_path, route_name, EndpointAction(route_method, mimetype), methods=options)

    def run(self) -> None:
        print('Starting webApp')
        self.add_route('/health_check', 'health_check', route.health_check, 'text/plain', ['GET'])
        self.app.run(host='0.0.0.0', port=5000, debug=False)
