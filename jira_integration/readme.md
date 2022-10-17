# PRE-REQS
This script requires a file in the same directory called

jira_cfg.json

The contents of that file should be: 

````
{
    "tenant": "<your jira tenant name. e.g. https://{YOUR_COMPANY}.atlassin.net>",
    "api_key": "<api key>",
    "user_id": "<admin user id>",
    "project_key": "<project key>"
}
````

###  PORTS
5601 (Kibana web interface).

9200 (Elasticsearch JSON interface).

5044 (Logstash Beats interface, receives logs from Beats such as Filebeat – see the Forwarding logs with Filebeat section).

From: https://elk-docker.readthedocs.io/
