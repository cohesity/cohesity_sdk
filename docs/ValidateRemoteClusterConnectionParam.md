# ValidateRemoteClusterConnectionParam

Specifies the parameters to update a Remote Cluster config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_addresses** | **List[str]** | Specifies the VIP or IP addresses of the Nodes on the Remote Cluster to connect with. Hostnames are not supported. | 
**password** | **str** | Specifies the password for Cohesity user to use when connecting to the Remote Cluster. | 
**username** | **str** | Specifies the Cohesity user name used to connect to the Remote Cluster. | 

## Example

```python
from cohesity_sdk.models.validate_remote_cluster_connection_param import ValidateRemoteClusterConnectionParam

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateRemoteClusterConnectionParam from a JSON string
validate_remote_cluster_connection_param_instance = ValidateRemoteClusterConnectionParam.from_json(json)
# print the JSON string representation of the object
print(ValidateRemoteClusterConnectionParam.to_json())

# convert the object into a dict
validate_remote_cluster_connection_param_dict = validate_remote_cluster_connection_param_instance.to_dict()
# create an instance of ValidateRemoteClusterConnectionParam from a dict
validate_remote_cluster_connection_param_from_dict = ValidateRemoteClusterConnectionParam.from_dict(validate_remote_cluster_connection_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


