import pygeoip

geoip = pygeoip.GeoIP("GeoLiteCity.dat")

res = geoip.record_by_addr('YOUR_IP-ADDRESS')

for key, val in res.items():
    print('%s : %s' % (key,val))