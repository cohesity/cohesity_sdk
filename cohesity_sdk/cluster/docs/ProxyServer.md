# ProxyServer

Specifies information about a proxy server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Specifies address of the proxy. This can be hostname or IP address. | 
**is_disabled** | **bool** | Specifies if the proxy configuration is disabled. | [optional] 
**name** | **str** | Specifies name of the proxy server. | [optional] 
**port** | **int** | Specifies port of the proxy. | 
**schemes** | **List[str]** | Specifies schemes of the proxy. | [optional] 
**services** | **List[str]** | Specifies the services to use the proxy. | [optional] 
**type** | **str** | Specifies type of the proxy. | [optional] 
**username** | **str** | Specifies user name of the proxy. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.proxy_server import ProxyServer

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyServer from a JSON string
proxy_server_instance = ProxyServer.from_json(json)
# print the JSON string representation of the object
print(ProxyServer.to_json())

# convert the object into a dict
proxy_server_dict = proxy_server_instance.to_dict()
# create an instance of ProxyServer from a dict
proxy_server_from_dict = ProxyServer.from_dict(proxy_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


