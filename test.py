from strobes_intel_client.main import client


response = client("CVE-2019-11477")
print(response.zeroday)
