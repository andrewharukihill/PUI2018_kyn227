from __future__ import print_function
# coding: utf-8

# In[6]:


import os
import json

import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
apikey=str(sys.argv[1])
bus_no=str(sys.argv[2])
print("Bus Line: "+ bus_no)
    

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+apikey+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_no
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[7]:


(type(data))


# In[8]:


data.keys()


# In[9]:


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=06f927d1-679b-4e09-9062-cb337838097e&VehicleMonitoringDetailLevel=calls&LineRef=B52"
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[10]:


data


# In[11]:
print ("Number of active buses: "+ str (len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])))

for bus in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    print ("Bus " + str(bus)+" is at latitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+ " and Longitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    


# In[12]:

