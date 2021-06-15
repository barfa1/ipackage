from iplocation import IpLocation

def test_iploc():
    ip = '157.34.29.75'
    obj = IpLocation()
    print(obj.get_country(ip))