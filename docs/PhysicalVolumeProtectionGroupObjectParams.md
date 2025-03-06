# PhysicalVolumeProtectionGroupObjectParams

Specifies object parameters for creating physical volume Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_system_backup** | **bool** | Specifies whether or not to take a system backup. Applicable only for windows sources. | [optional] 
**excluded_vss_writers** | **List[str]** | Specifies writer names which should be excluded from physical volume based backups for a given source. | [optional] 
**id** | **int** | Specifies the ID of the object protected. | 
**name** | **str** | Specifies the name of the object protected. | [optional] [readonly] 
**volume_guids** | **List[str]** | Specifies the list of GUIDs of volumes protected. If empty, then all volumes will be protected by default. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.physical_volume_protection_group_object_params import PhysicalVolumeProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalVolumeProtectionGroupObjectParams from a JSON string
physical_volume_protection_group_object_params_instance = PhysicalVolumeProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalVolumeProtectionGroupObjectParams.to_json())

# convert the object into a dict
physical_volume_protection_group_object_params_dict = physical_volume_protection_group_object_params_instance.to_dict()
# create an instance of PhysicalVolumeProtectionGroupObjectParams from a dict
physical_volume_protection_group_object_params_from_dict = PhysicalVolumeProtectionGroupObjectParams.from_dict(physical_volume_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


