# ProxyServerList

Specifies the list of proxy servers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proxy_servers** | [**List[ProxyServer]**](ProxyServer.md) | List of proxy servers. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.proxy_server_list import ProxyServerList

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyServerList from a JSON string
proxy_server_list_instance = ProxyServerList.from_json(json)
# print the JSON string representation of the object
print(ProxyServerList.to_json())

# convert the object into a dict
proxy_server_list_dict = proxy_server_list_instance.to_dict()
# create an instance of ProxyServerList from a dict
proxy_server_list_from_dict = ProxyServerList.from_dict(proxy_server_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


