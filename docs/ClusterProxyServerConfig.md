# ClusterProxyServerConfig

Specifies the parameters of the proxy server to be used for external traffic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Specifies the IP address of the proxy server. | 
**is_disabled** | **bool** | Disable proxy is used to turn the proxy on and off. | [optional] 
**name** | **str** | Specifies the unique name of the proxy server. | [optional] [readonly] 
**password** | **str** | Specifies the password for the proxy. | [optional] 
**port** | **int** | Specifies the port on which the server is listening. | 
**username** | **str** | Specifies the username for the proxy. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_proxy_server_config import ClusterProxyServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProxyServerConfig from a JSON string
cluster_proxy_server_config_instance = ClusterProxyServerConfig.from_json(json)
# print the JSON string representation of the object
print(ClusterProxyServerConfig.to_json())

# convert the object into a dict
cluster_proxy_server_config_dict = cluster_proxy_server_config_instance.to_dict()
# create an instance of ClusterProxyServerConfig from a dict
cluster_proxy_server_config_from_dict = ClusterProxyServerConfig.from_dict(cluster_proxy_server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


