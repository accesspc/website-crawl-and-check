# Changes

## TO DO

* feat: send email for status changes
* feat: crawl website for pages
* feat: collect page metrics and display generate report(s)
* feat: run SAST scanner

## History

### v0.0.1

Init:

* main - init config and state, loop config and collect status for each page
* lib/config - build a config object built from config.yml
* lib/email - send email based on ok / error templates
* lib/service - init a session and perform GET and POST requests
* lib/state - read, build and store state to a file
