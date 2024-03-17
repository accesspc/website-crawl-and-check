# Changes

## TO DO

* feat: send email for status changes
* feat: crawl website for pages
* feat: collect page metrics and display generate report(s)
* feat: run SAST scanner
* fix: secure nfs volume

## History

### v2.0.0

* Refactored from CronJob to a Flask app with APScheduler inside
* Metrics printed out on /metrics
* Updated Helm chart

### v1.0.1

Fix:

* NFS mount point
* Cleaned up naming

### v1.0.0

Release:

* App working on local machine using `docker compose` and in K8s

### v0.0.3

Fix:

* Status output to include request timestamp

### v0.0.2

Update:

* Move config.yml and state.json to separate folders for better mounting options

### v0.0.1

Init:

* main - init config and state, loop config and collect status for each page
* lib/config - build a config object built from config.yml
* lib/email - send email based on ok / error templates
* lib/service - init a session and perform GET and POST requests
* lib/state - read, build and store state to a file
