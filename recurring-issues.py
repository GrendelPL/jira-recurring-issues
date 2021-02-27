import json
import os
import sys
from jira import JIRA
import collections
from collections import Counter, OrderedDict
from datetime import datetime

def argument_handler():
    
    tickets_list =[]

    username =  os.environ.get('JIRA_USER')
    password =  os.environ.get('JIRA_PASS')
    server = os.environ.get('JIRA_URL')

    jira = JIRA(
        basic_auth=(username,password),
        options= {
            'server' : server
            }
       )

    issues = []
  
    jql = 'category = support AND createdDate > startOfMonth()'
  
    block_size = 100
    block_num = 0
    i = 0
    
    while True:
        start_idx = block_num * block_size
        if block_num == 0:
            issues = jira.search_issues(jql, start_idx, block_size)
        else:
            more_issues = jira.search_issues(jql, start_idx, block_size)
            if len(more_issues)>0:
                for x in more_issues:
                    issues.append(x)
            else:
                break
        if len(issues) == 0:
            # Retrieve issues until there are no more to come
            break
        block_num += 1
    print(len(issues))

    for issue in issues:     
        subject = issue.fields.summary

        #if your alarms have different prefixes/suffixes, that't the place to filter them out.
        subject = subject.replace(' is UP **','')
        subject = subject.replace(' is DOWN **','')
        tickets_list.append(subject)

    timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    filename = 'duplications-' + timestamp + '.txt'
    with open(filename,'w',encoding='utf-8') as filehandle:
        all_together = collections.Counter(tickets_list).most_common()
        for s in all_together:
            print(*s)
            line = ''.join(str(s))
            withnewline = line+'\n'
            filehandle.write(withnewline)

def main():
    argument_handler()
      
if __name__ == '__main__':
    main()