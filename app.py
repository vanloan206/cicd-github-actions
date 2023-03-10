# from wsgiref.simple_server import make_server
# from pyramid.config import Configurator
# from pyramid.response import Response
# import os

# def hello_world(request):
#     name = os.environ.get('NAME')
#     if name == None or len(name) == 0:
#         name = "world"
#     message = "Hello, " + name + "!\n"
#     return Response(message)

# if __name__ == '__main__':
#     port = int(os.environ.get("PORT"))
#     with Configurator() as config:
#         config.add_route('hello', '/')
#         config.add_view(hello_world, route_name='hello')
#         app = config.make_wsgi_app()
#     server = make_server('0.0.0.0', port, app)
#     server.serve_forever()


"""Base example application."""
import socket

import flask


def create_app():
    app = flask.Flask(__name__)

    @app.route('/health')
    def base_healthcheck_route():
        """Healthcheck route."""
        return {"message": "flask is operational", "error": False}, 200

    @app.route('/')
    def index():
        """Example route."""
        message = f"Hello from {socket.gethostname()}"
        return {"message": message}, 200

    return app

def main():
    """Main entrypoint."""
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=80)


if __name__ == "__main__":
    main()
