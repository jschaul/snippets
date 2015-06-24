#/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on May 30, 2013

@author: jschaul


install dependencies via "sudo pip install pycrypto jira-python"
(see : http://jira-python.readthedocs.org/en/latest/ )

'''

#change this value accordingly:
SERVER = 'https://<your-name>.atlassian.net'


import datetime
from jira.client import JIRA
import argparse


HOURSECONDS = 3600
    
print datetime.datetime.now()
    
parser = argparse.ArgumentParser()

parser.add_argument('-p', '--password', help="jira password") 
parser.add_argument('-u', '--username', help="jira username") 
parser.add_argument('-s', '--sprintname', help="full name of the sprint") 

args = parser.parse_args()
AUTH = (args.username, args.password)

    
def main():

    print "Starting..."
    jira = JIRA(options={'server': SERVER}, basic_auth=AUTH)    # a username/password tuple

    sprint = jira.search_issues('sprint = "'+args.sprintname+'"')
    with open('{}.txt'.format(args.sprintname), 'wb') as f: 
	parentList = []
        for i in sprint:
            issue = jira.issue(i.key)
   	    try:
		parentList.append(issue.fields.parent.key)
	    except:
		pass
            f.write(issue.key.encode('utf8') + '\n') 
            f.write(issue.fields.summary.encode('utf8') + '\n') 
            f.write('\n') 
            if issue.fields.description:
                f.write(issue.fields.description.encode('utf8').strip().replace("\t", "").replace("\r", "").replace("\n\n", "\n") + '\n\n') 
            f.write(getstorypoints(issue))
            
            f.write('\n'.join(["" for i in range(5)]))
	parents = set(parentList)
	f.write("--------------------")
	for i in parents:
	    issue = jira.issue(i)
            f.write(issue.key.encode('utf8') + '\n') 
            f.write(issue.fields.summary.encode('utf8') + '\n') 
            f.write('\n') 
            if issue.fields.description:
                f.write(issue.fields.description.encode('utf8').strip().replace("\t", "").replace("\r", "").replace("\n\n", "\n") + '\n\n') 
            f.write(getstorypoints(issue))
            
            f.write('\n'.join(["" for i in range(5)]))
	
	    
    print 'writing complete'



def getstorypoints(issue):
    try:
        return "Estimate: " + str(int(issue.raw['fields']['customfield_10004']))
    except:
        return "(estimate?)"
    #return str({"estimate":issue.raw['fields']['customfield_10004'], 'all':issue.raw['fields'], 'remaining':issue.raw['fields']['aggregatetimeestimate'], 'spent':issue.raw['fields']['aggregatetimespent'], 'estimate':issue.raw['fields']['aggregatetimeoriginalestimate']})
    

if __name__ == '__main__':
#    all()
    main()
    
    
    

