# metrics.py
import time
import psutil
from flask import request
from prometheus_client import Gauge, Counter, Histogram, generate_latest

# Counter metric for counting the total number of requests
request_counter = Counter('app_requests_total', 'Total number of requests')

# Histogram metric for measuring the response time of requests
request_duration_histogram = Histogram('app_request_duration_seconds', 'Request duration in seconds')

# Gauge metric for monitoring the memory usage of the application process
memory_usage_gauge = Gauge('app_memory_usage_bytes', 'Memory usage in bytes')

# Gauge metric for monitoring the number of active threads in the application
active_threads_gauge = Gauge('app_active_threads', 'Number of active threads')

def register_metrics(app, app_version, app_config):
    @app.before_request
    def before_request():
        # Increment the request counter before each request
        request_counter.inc()

        # Record the start time for measuring request duration
        request._prometheus_metrics_start_time = time.time()

    @app.after_request
    def after_request(response):
        # Measure the request duration and record it in the histogram
        duration = time.time() - request._prometheus_metrics_start_time
        request_duration_histogram.observe(duration)

        return response

    @app.route('/metrics')
    def metrics():
        # Update the memory usage gauge with the current memory usage
        memory_usage_gauge.set(psutil.Process().memory_info().rss)

        # Update the active threads gauge with the current number of threads
        active_threads_gauge.set(psutil.cpu_count(logical=False))

        # Return Prometheus metrics in the /metrics endpoint
        return generate_latest()

    # Add more metrics and monitoring logic as needed
