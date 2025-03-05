# ViewProtectionGroupReplicationParams

Specifies the parameters for view replication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_name_config_list** | [**List[ReplicatedViewNameConfig]**](ReplicatedViewNameConfig.md) | Specifies the list of remote view names for the protected views in the Protection Group. By default the names will be the same as the name of the protected view. | [optional] 

## Example

```python
from cohesity_sdk.models.view_protection_group_replication_params import ViewProtectionGroupReplicationParams

# TODO update the JSON string below
json = "{}"
# create an instance of ViewProtectionGroupReplicationParams from a JSON string
view_protection_group_replication_params_instance = ViewProtectionGroupReplicationParams.from_json(json)
# print the JSON string representation of the object
print(ViewProtectionGroupReplicationParams.to_json())

# convert the object into a dict
view_protection_group_replication_params_dict = view_protection_group_replication_params_instance.to_dict()
# create an instance of ViewProtectionGroupReplicationParams from a dict
view_protection_group_replication_params_from_dict = ViewProtectionGroupReplicationParams.from_dict(view_protection_group_replication_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


