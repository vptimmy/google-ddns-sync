# google-ddns-sync

Create a secret for the google DDNS username and password.  Your google Dynamic DNS username and password can be  
viewed by looking at "View Credentials" under Advanced Dynamic DNS at domains.google.com.  Do not use your  
Google username and password.


`kubectl create secret gmail-ddns-credentials --from-literal=username=*YOUR USERNAME* --from-literal=password=*YOUR PASSWORD*`

Then deploy it to your K8 cluster
`skaffold deploy`
