import pygeoip #pip3 install pygeoip

#GeoLiteCity.dat File is included in same Folder 
geoip = pygeoip.GeoIP("GeoLiteCity.dat")
res = geoip.record_by_addr('42.201.208.125')

for key, val in res.items():
    print('%s : %s' % (key,val))
