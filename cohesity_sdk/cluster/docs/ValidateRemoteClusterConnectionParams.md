# ValidateRemoteClusterConnectionParams

Specifies the parameters to update a Remote Cluster config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_addresses** | **List[str]** | Specifies the VIP or IP addresses of the Nodes on the Remote Cluster to connect with. Hostnames are not supported. | 
**password** | **str** | Specifies the password for Cohesity user to use when connecting to the Remote Cluster. | 
**username** | **str** | Specifies the Cohesity user name used to connect to the Remote Cluster. | 

## Example

```python
from cohesity_sdk.cluster.models.validate_remote_cluster_connection_params import ValidateRemoteClusterConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateRemoteClusterConnectionParams from a JSON string
validate_remote_cluster_connection_params_instance = ValidateRemoteClusterConnectionParams.from_json(json)
# print the JSON string representation of the object
print(ValidateRemoteClusterConnectionParams.to_json())

# convert the object into a dict
validate_remote_cluster_connection_params_dict = validate_remote_cluster_connection_params_instance.to_dict()
# create an instance of ValidateRemoteClusterConnectionParams from a dict
validate_remote_cluster_connection_params_from_dict = ValidateRemoteClusterConnectionParams.from_dict(validate_remote_cluster_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


