# DgRoleBasedBackup

Control the Oracle Data Guard role based backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_backup_archivelog_on_any_role** | **bool** | Specifies if the archive log backup is allowed on all the roles. | [optional] [default to False]
**backup_on_dg_role** | **str** | Specifies the Data Guard role for which backup is allowed. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.dg_role_based_backup import DgRoleBasedBackup

# TODO update the JSON string below
json = "{}"
# create an instance of DgRoleBasedBackup from a JSON string
dg_role_based_backup_instance = DgRoleBasedBackup.from_json(json)
# print the JSON string representation of the object
print(DgRoleBasedBackup.to_json())

# convert the object into a dict
dg_role_based_backup_dict = dg_role_based_backup_instance.to_dict()
# create an instance of DgRoleBasedBackup from a dict
dg_role_based_backup_from_dict = DgRoleBasedBackup.from_dict(dg_role_based_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


