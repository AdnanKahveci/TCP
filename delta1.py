import json
import numpy as np
from pprint import pprint

with open("/home/adnan/Downloads/mikrohelper-main/data.json") as f:
    data=json.load(f)


# pprint(dict)
dst="93.94.251.206"
flow = data['-52136525125092253248843697872869714919']['flow']


for item in flow :
   if item['tcp_headers']['tcp_syn_f'] is True and item['tcp_headers']['tcp_ack_f'] is False:
      for i in range(3):
        flow.pop(0)


psh_ack_listesi=[]
ack_listesi = []

for key,value in data.items():
    if value['flow'][0]['ip_destination_address'] == dst:
        flow=value['flow']
        for item in flow:
            if  item['tcp_headers']['tcp_psh_f'] is True and item['tcp_headers']['tcp_ack_f'] is True:
                # print(item)
                next_ack = item['tcp_headers']['tcp_sequence_number'] + item['tcp_headers']['tcp_window_size']

                # print(item['timestamp'],item['tcp_headers']['tcp_ack_number'],item['tcp_headers']['tcp_sequence_number'],item['tcp_headers']['tcp_window_size'],"Next ack num=",next_ack)
                psh_ack_listesi.append((item['timestamp'], item['tcp_headers']['tcp_sequence_number'],"bir sonraki ack",next_ack))


for key,value in data.items():
    if value['flow'][0]['ip_destination_address'] == dst:
        flow=value['flow']
        for item in flow:
            if  item['tcp_headers']['tcp_psh_f'] is False and item['tcp_headers']['tcp_ack_f'] is True:
                # print(item['tcp_headers']['tcp_sequence_number'])
                ack_listesi.append((item['timestamp'],item['tcp_headers']['tcp_ack_number']))

for item in psh_ack_listesi:
    print(item)
for ack in ack_listesi:
    print(ack)

for item in psh_ack_listesi:
    for ack in ack_listesi:
        if item[2]==ack[1]:
            print(item[0]-ack[0])
