import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8076')}"
# Heroku dynos have limited memory; deriving workers from the host CPU count
# can start hundreds of processes and make the dyno crash during boot.
workers = int(os.environ.get("WEB_CONCURRENCY", "2"))
worker_class = "gevent"
worker_connections = 500
timeout = 120
graceful_timeout = 30
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info"
proc_name = "tsun-ff-infoxvisits"
# Importing the app in each worker avoids a preload failure taking down the
# entire dyno and keeps startup compatible with gevent monkey-patching.
preload_app = False
limit_request_line = 8190
limit_request_fields = 100
limit_request_field_size = 8190
max_requests = 5000
max_requests_jitter = 500
