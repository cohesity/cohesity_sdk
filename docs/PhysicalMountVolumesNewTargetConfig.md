# PhysicalMountVolumesNewTargetConfig

Specifies the configuration for mounting volumes to a new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**server_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.physical_mount_volumes_new_target_config import PhysicalMountVolumesNewTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalMountVolumesNewTargetConfig from a JSON string
physical_mount_volumes_new_target_config_instance = PhysicalMountVolumesNewTargetConfig.from_json(json)
# print the JSON string representation of the object
print(PhysicalMountVolumesNewTargetConfig.to_json())

# convert the object into a dict
physical_mount_volumes_new_target_config_dict = physical_mount_volumes_new_target_config_instance.to_dict()
# create an instance of PhysicalMountVolumesNewTargetConfig from a dict
physical_mount_volumes_new_target_config_from_dict = PhysicalMountVolumesNewTargetConfig.from_dict(physical_mount_volumes_new_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


