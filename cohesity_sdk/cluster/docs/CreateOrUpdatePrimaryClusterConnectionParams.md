# CreateOrUpdatePrimaryClusterConnectionParams

Specifies the params to initialize the pairing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password for Cohesity user to use when connecting to the cluster. | 
**username** | **str** | Specifies the Cohesity user name used to connect to the cluster. | 
**all_endpoints_reachable** | **bool** | Specifies if all endpoints on Primary Cluster are reachable. | [optional] [default to False]
**network_interface** | **str** | Specifies the name of the network interfaces to use for communicating with the Remote Cluster. | [optional] 
**node_addresses** | **List[str]** | Specifies the VIP or IP addresses of the Nodes on the Primary Cluster to connect with. Hostnames are not supported. | 

## Example

```python
from cohesity_sdk.cluster.models.create_or_update_primary_cluster_connection_params import CreateOrUpdatePrimaryClusterConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdatePrimaryClusterConnectionParams from a JSON string
create_or_update_primary_cluster_connection_params_instance = CreateOrUpdatePrimaryClusterConnectionParams.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdatePrimaryClusterConnectionParams.to_json())

# convert the object into a dict
create_or_update_primary_cluster_connection_params_dict = create_or_update_primary_cluster_connection_params_instance.to_dict()
# create an instance of CreateOrUpdatePrimaryClusterConnectionParams from a dict
create_or_update_primary_cluster_connection_params_from_dict = CreateOrUpdatePrimaryClusterConnectionParams.from_dict(create_or_update_primary_cluster_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


