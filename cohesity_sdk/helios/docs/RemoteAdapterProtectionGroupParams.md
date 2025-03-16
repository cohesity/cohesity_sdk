# RemoteAdapterProtectionGroupParams

Specifies the parameters which are specific to Remote Adapter related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. | [optional] 
**hosts** | [**List[RemoteAdapterHost]**](RemoteAdapterHost.md) | Specifies a list of hosts to protected in this protection group. | 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**remote_view_params** | [**RemoteAdapterProtectionGroupReplicationParams**](RemoteAdapterProtectionGroupReplicationParams.md) |  | [optional] 
**view_id** | **int** | Specifies the id of the view where we put the script result data. | 

## Example

```python
from cohesity_sdk.helios.models.remote_adapter_protection_group_params import RemoteAdapterProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteAdapterProtectionGroupParams from a JSON string
remote_adapter_protection_group_params_instance = RemoteAdapterProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(RemoteAdapterProtectionGroupParams.to_json())

# convert the object into a dict
remote_adapter_protection_group_params_dict = remote_adapter_protection_group_params_instance.to_dict()
# create an instance of RemoteAdapterProtectionGroupParams from a dict
remote_adapter_protection_group_params_from_dict = RemoteAdapterProtectionGroupParams.from_dict(remote_adapter_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


