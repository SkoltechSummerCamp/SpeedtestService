from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()


def post_to_server(port=5201):
    body = swagger_client.ServerAddr(port=port) # ServerAddr | port of iperf server. Ip and time could be emply (optional)
    try:
        # post self ip to balancer
        api_instance.server_post_ip(body=body)
    except ApiException as e:
        print("Exception when calling ServerApi->server_post_ip: %s\n" % e)