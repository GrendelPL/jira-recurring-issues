# jira

## Requirements:
System variables need to be in place to authenticate in Jira:

JIRA_URL=http://account.atlassian.net/<br>
JIRA_USER=email@account.com<br>
JIRA_PASS=token generated in jira settings<br>

## Installation of dependencies
python -m pip install -r requirements.txt
(or) pip install -r requirements.txt

## Usage:
jql variable holds the JQL query of your choosing - no validation so the query must be valid. Otherwise your output will be 0. If no tickets returning, check your system variables first (usual cause of problems), once you confirm that connection is fine, focus on your query - test it in jira intgerface first.

