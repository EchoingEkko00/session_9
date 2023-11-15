curl -D- \
   -X GET \
   -H "Authorization: Basic bGFjb3VmQGdtYWlsLmNvbTozY2dqWnkxcTJIbTJReHh2akhLQTYwQ0Y=" \
   -H "Content-Type: application/json" \
   "https://420-565-a21-1.atlassian.net/rest/api/3/search?jql=project%20=%20%22EQ1%22%20AND%20timespent%20!=%200&maxResults=500&fields=id,worklog,parent,summary"

