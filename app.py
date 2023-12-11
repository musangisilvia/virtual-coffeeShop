from flaskr import app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from prometheus_client import make_wsgi_app
from flaskr.metrics import register_metrics  

# Register metrics
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

if __name__ == "__main__":
    # Run the application with metrics
    run_simple(hostname="0.0.0.0", port=5000, application=dispatcher, use_reloader=True, use_debugger=True)
