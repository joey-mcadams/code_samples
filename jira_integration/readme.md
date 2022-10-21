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
Install requirements with `pip install -r requirements.txt`

### TO USE (In progress)
Run the following script. 

`python3 main.py`

Give the script a bit to start up and view results here.

`http://localhost:5000`

### PORTS
5601 - Kibana web interface.

9200 - Elasticsearch JSON interface.

5044 - Logstash Beats interface, receives logs from Beats such as Filebeat – see the Forwarding logs with Filebeat section.

5000 - Flask

From: https://elk-docker.readthedocs.io/

### OUTPUT 
It may take a minute or two for the first few tickets to hit the Elastic. The output should let you know when the 
first high and higher tickets hit the queue. Once that happens, the end graph can be viewed here: 

http://localhost:5000

### RANDOM THOUGHTS / TODOS
If writing this project again from start. Elastic, Jira, and Flask should all be client classes. It should 
really be a 3 tier MVC style design.

Many of the configuration options have been hard coded for speed. They should be externalized (ticket priority, speed 
of ticket creation for examples)