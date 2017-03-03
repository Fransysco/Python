import requests

url = "https://X.X.X.X:9060/ers/config/networkdevice/bulk/submit"
meow = open('nad.xml', 'r')
meow2 = meow.read()
meow3 = ET.fromstring(meow2)
payload =  ET.tostring(meow3, encoding='utf-8', method='xml')

headers = {
    'content-type': "application/vnd.com.cisco.ise.network.networkdevicebulkrequest.1.1+xml",
    'authorization': "Basic XXXXXXXXXXXXXXXXXXXXXX",
    'cache-control': "no-cache"
}
response = requests.request("PUT", url, data=payload, headers=headers, verify=False)

#Response manipulation
responselocation = response.headers['location']
bulkstatusid = responselocation.split("submit/",1)[1]

#Print BulkID
print ("Bulk ID:" + str(bulkstatusid)
