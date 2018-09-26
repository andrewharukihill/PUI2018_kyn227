
# coding: utf-8

# In[1]:


import pylab as pl
import traceback
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

get_ipython().run_line_magic('pylab', 'inline')
pl.rc('font', size=15)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=06f927d1-679b-4e09-9062-cb337838097e&VehicleMonitoringDetailLevel=calls&LineRef=B52"
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[2]:


(type(data))


# In[3]:


data.keys()


# In[4]:


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=06f927d1-679b-4e09-9062-cb337838097e&VehicleMonitoringDetailLevel=calls&LineRef=B52"
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[10]:


data


# In[22]:


data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']


# In[27]:


data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']


# In[ ]:


(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])


# In[42]:


for bus in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    print("Bus " + str(bus)+" is at Latitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+ " and Longitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    
    if bool(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']):
        print(str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']))
        print(str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']))
    else:
        print('N/A')
        print('N/A')
    


# In[45]:


Lat=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])


# In[46]:


print(Lat)


# In[48]:





# In[49]:


print(Long)


# In[53]:


StopName=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])


# In[54]:


print(StopName)


# In[55]:


StopPoint=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])


# In[56]:


print(StopPoint)


# In[58]:


for bus in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    #print("Bus " + str(bus)+" is at Latitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+ " and Longitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    Lat=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    Long=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        
    if bool(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']):
        StopPoint=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
        StopName=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        print(Lat+","+Long+","+StopPoint+","+StopName)
        
    else:
        print(Lat+","+Long+","+'N/A,N/A')
       
    


# In[ ]:


for bus in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    #print("Bus " + str(bus)+" is at Latitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+ " and Longitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    Lat=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    Long=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        
    if bool(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']):
        StopPoint=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
        StopName=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        (Lat+","+Long+","+StopPoint+","+StopName)
        
    else:
        print(Lat+","+Long+","+'N/A,N/A')

