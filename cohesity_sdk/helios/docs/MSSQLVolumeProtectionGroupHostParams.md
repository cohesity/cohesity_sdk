# MSSQLVolumeProtectionGroupHostParams

Specifies the host specific parameters for a host container in this protection group. Objects specified here should only be MSSQL root containers and will not be protected unless they are also specified in the 'objects' list. This list is just for specifying source level settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_system_backup** | **bool** | Specifies whether to enable system/bmr backup using 3rd party tools installed on agent host. | [optional] 
**host_id** | **int** | Specifies the id of the host container on which databases are hosted. | 
**host_name** | **str** | Specifies the name of the host container on which databases are hosted. | [optional] [readonly] 
**volume_guids** | **List[str]** | Specifies the list of volume GUIDs to be protected. If not specified, all the volumes of the host will be protected. Note that volumes of host on which databases are hosted are protected even if its not mentioned in this list. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mssql_volume_protection_group_host_params import MSSQLVolumeProtectionGroupHostParams

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLVolumeProtectionGroupHostParams from a JSON string
mssql_volume_protection_group_host_params_instance = MSSQLVolumeProtectionGroupHostParams.from_json(json)
# print the JSON string representation of the object
print(MSSQLVolumeProtectionGroupHostParams.to_json())

# convert the object into a dict
mssql_volume_protection_group_host_params_dict = mssql_volume_protection_group_host_params_instance.to_dict()
# create an instance of MSSQLVolumeProtectionGroupHostParams from a dict
mssql_volume_protection_group_host_params_from_dict = MSSQLVolumeProtectionGroupHostParams.from_dict(mssql_volume_protection_group_host_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


