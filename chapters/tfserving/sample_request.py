import base64

import requests

data = b"\n\xb1\x05\n/\n\x10company_response\x12\x1b\n\x19\n\x17Closed with explanation\n\x1a\n\x0ftimely_response\x12\x07\n\x05\n\x03Yes\n \n\x0bsub_product\x12\x11\n\x0f\n\rI do not know\n\x15\n\x08zip_code\x12\t\n\x07\n\x05480XX\n\x0f\n\x05state\x12\x06\n\x04\n\x02MI\n2\n\x05issue\x12)\n'\n%Cont'd attempts collect debt not owed\n!\n\tsub_issue\x12\x14\n\x12\n\x10Debt is not mine\n$\n\x07company\x12\x19\n\x17\n\x15Stellar Recovery Inc.\n\xde\x02\n\x1cconsumer_complaint_narrative\x12\xbd\x02\n\xba\x02\n\xb7\x02Almost daily phone calls from Stellar Recovery for months now. All computer calls.   I own my home, own my car, pay my credit card bill monthly, as well as utility bills, insurance, etc.   I have a stellar credit rating, clean credit record, and owe money to no one. Obviously, this is unwarranted harassment.  \n\x1e\n\x07product\x12\x13\n\x11\n\x0fDebt collection\n\x1a\n\x11consumer_disputed\x12\x05\x1a\x03\n\x01\x01"  # noqa: E501

payload = {"instances": [{"examples": {"b64": base64.b64encode(data).decode("utf-8")}}]}
# Please change the model name
url = "http://127.0.0.1:8501/v1/models/model:predict"
response = requests.post(url, json=payload)
print(response.json())
