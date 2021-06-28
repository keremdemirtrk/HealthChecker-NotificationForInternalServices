from slack_sdk.webhook import WebhookClient
import urllib3
import requests
http = urllib3.PoolManager()

InternalServicesList = ["service1", "service2", "service3"] # You can add as many service urls as you want
SendNotificationUrl = "slack-hook-url" # you must add slack hook url

for ListInternalServices in InternalServicesList:
    r =  http.request('GET', ListInternalServices)
    print(r.status)
    if r.status != 200:
        print(ListInternalServices)   
    webhook = WebhookClient(SendNotificationUrl)
    text1 = ListInternalServices
    response = webhook.send(text= text1 + " Servisi düştü")

