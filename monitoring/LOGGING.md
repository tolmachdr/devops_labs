# Logging

Grafana, Loki, and Promtail.

## Components:

### Loki: 
Stores logs. It’s lightweight and uses labels for efficient querying.

### Promtail: 
Collects logs from Docker containers (/var/lib/docker/containers) and the host system (/var/log), then sends them to Loki.

### Grafana: 
Visualizes logs stored in Loki. It’s configured to use Loki as a datasource.

### Python & Go Apps: 
Generate logs, which are collected by Promtail.

## How It Works:
Logs are generated by the Python and Go apps.

Promtail collects these logs and sends them to Loki.

Loki stores the logs and makes them queryable.

Grafana connects to Loki, allowing you to visualize and analyze the logs via dashboards.

Access:
Grafana: http://localhost:3000

Loki: http://localhost:3100

Python App: http://localhost:8081

Go App: http://localhost:8082

## Logging screenshots

![img](/attachments/img_4.png)

![img](/attachments/img_5.png)

![img](/attachments/img_6.png)
![img](/attachments/img_7.png)
