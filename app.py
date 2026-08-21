from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Инициализация метрик Prometheus
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'DevOps Resume Application', version='1.0.0')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
