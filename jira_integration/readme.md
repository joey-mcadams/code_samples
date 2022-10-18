### PRE-REQS
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

### SETUP
Run the `get_start_elk.sh` script to get the required docker container and start it. 

### TO USE (In progress)
Run the following scripts. 

`python3 jira_ticket_maker.py`

In a separate terminal

`python3 jira_ticket_getter.py`

That will start feeding Jira random tickets and pushing the High and Highest tickets into the ELK container. 

Results can be viewed in Kibana with a simple graph (will be updated). 

###  PORTS
5601 - Kibana web interface.

9200 - Elasticsearch JSON interface.

5044 - Logstash Beats interface, receives logs from Beats such as Filebeat – see the Forwarding logs with Filebeat section.

5000 - Flask

From: https://elk-docker.readthedocs.io/
