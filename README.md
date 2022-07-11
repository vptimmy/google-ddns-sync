# google-ddns-sync


This cronjob will run every 10 minutes and update your Google DDNS with your home router IP address. Edit [cronjob.yaml](cronjob.yaml) to modify the cronjob schedule. 


Create a secret for the google DDNS username and password.  Your google Dynamic DNS username and password can be viewed by looking at "View Credentials" under Advanced Dynamic 
DNS at [domains.google.com](https://domains.google.com).  Do not use your Google username and password!


`kubectl create secret generic google-ddns-credentials --from-literal=username=*YOUR USERNAME* --from-literal=password=*YOUR PASSWORD*`


Deploy to your Kubernetes cluster  
`skaffold deploy`
