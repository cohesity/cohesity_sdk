# RemoteAdapterProtectionGroupReplicationParams

Specifies the parameters for Remote Adapter replication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_view** | **bool** | Specifies whether or not to create a remote view on replication cluster. | 
**view_name** | **str** | Specifies the name of the remote view. By default the name will be same as the protected view. If a view with the specified name already exists on the remote cluster, the created name will have a suffix &#39;-1&#39;. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.remote_adapter_protection_group_replication_params import RemoteAdapterProtectionGroupReplicationParams

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteAdapterProtectionGroupReplicationParams from a JSON string
remote_adapter_protection_group_replication_params_instance = RemoteAdapterProtectionGroupReplicationParams.from_json(json)
# print the JSON string representation of the object
print(RemoteAdapterProtectionGroupReplicationParams.to_json())

# convert the object into a dict
remote_adapter_protection_group_replication_params_dict = remote_adapter_protection_group_replication_params_instance.to_dict()
# create an instance of RemoteAdapterProtectionGroupReplicationParams from a dict
remote_adapter_protection_group_replication_params_from_dict = RemoteAdapterProtectionGroupReplicationParams.from_dict(remote_adapter_protection_group_replication_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


