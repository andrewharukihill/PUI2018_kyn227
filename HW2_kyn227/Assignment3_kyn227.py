
# coding: utf-8

# In[6]:


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


data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']


# In[12]:


len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

