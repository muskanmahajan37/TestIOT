from boltiot import Bolt
api_key = "f04bfd50-9d89-42a8-a957-ff2cfe9fd930"
device_id = "BOLT6098139"
mybolt = Bolt(api_key, device_id)
response = mybolt.digitalWrite('0', 'LOW')
print (response)
