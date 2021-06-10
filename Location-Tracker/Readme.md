# Location Tracker Python

*Firstly you have to to install a very important Module called pygeoip*

_**You can install pygeip by executing this command :**_

```
$ pip3 install pygeoip
```
# Usage
*Insert Your Target IP Address (of which location you wanna know) here*

```
res = geoip.record_by_addr('Your-Target-IP')
```
## For Example 

```
res = geoip.record_by_addr('201.108.48.125')
```
# Results

```
dma_code : 0
area_code : 0
metro_code : None
postal_code : Postal Code
country_code : Country code
country_code3 : Contry Code 3
country_name : Country Name
continent : Continent Name
region_code : Regin's Code
city : City's Name
latitude : Location's Latitude
longitude : Locaton's Longitude
time_zone : Continent/City
```