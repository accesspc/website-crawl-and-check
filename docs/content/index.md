# App

Website Crawl and Check is a little app that crawls the website for internal links and then keeps a status track of them

## Config file

Before running locally or deploying using Docker, K8s or Helm, make sure config file exist:

* config/config.yml

If not, create from sample file included in the repo:

* config/config.sample.yml

```yaml
---

cron:
  seconds: 15

email:
  msg:
    ok:
      h1: OK
      h1_color: green
      status: up
    warn:
      h1: WARNING !!!
      h1_color: red
      status: down
  recipients:
    - developer@example.com
  sender: alert@example.com
  server: 192.168.1.2

websites:
  - id: example.com
    crawl: false
    paths:
      - /
      - /blog/
      - /wp-login.php
    proto: https
    timeout: 5
```
