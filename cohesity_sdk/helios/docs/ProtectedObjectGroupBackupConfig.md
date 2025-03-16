# ProtectedObjectGroupBackupConfig

Specifies the parameters of a protection group which is protecting an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_group_id** | **str** | Specifies the protection group id, if given object is also protected by a protection group. | [optional] 
**protection_group_name** | **str** | Specifies the protection group name, if given object is also protected by a protection group. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.protected_object_group_backup_config import ProtectedObjectGroupBackupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectGroupBackupConfig from a JSON string
protected_object_group_backup_config_instance = ProtectedObjectGroupBackupConfig.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectGroupBackupConfig.to_json())

# convert the object into a dict
protected_object_group_backup_config_dict = protected_object_group_backup_config_instance.to_dict()
# create an instance of ProtectedObjectGroupBackupConfig from a dict
protected_object_group_backup_config_from_dict = ProtectedObjectGroupBackupConfig.from_dict(protected_object_group_backup_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


