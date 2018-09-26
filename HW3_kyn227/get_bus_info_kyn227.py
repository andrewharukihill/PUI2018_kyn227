from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_kyn227.py <MTA_KEY> <BUS_LINE> bus_line.csv")
    sys.exit()

fout = open(sys.argv[3], "w")
print("Latitude,Longitude,Stop Name,Stop Status\n")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
apikey=str(sys.argv[1])
bus_no=str(sys.argv[2])
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+apikey+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_no

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


(type(data))


data.keys()

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+apikey+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_no

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)



for bus in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    #print("Bus " + str(bus)+" is at Latitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+ " and Longitude "+str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    Lat=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    Long=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
        
    if bool(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']):
        StopPoint=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][bus]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
        StopName=str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        print(Lat+","+Long+","+StopPoint+","+StopName)
        fout.write(Lat+","+Long+","+StopPoint+","+StopName+"\n")
        
    else:
        print(Lat+","+Long+","+'N/A,N/A')
        fout.write(Lat+","+Long+","+'N/A,N/A\n')

