# PhysicalMountVolumesOriginalTargetConfig

Specifies the configuration for mounting volumes to the original target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.physical_mount_volumes_original_target_config import PhysicalMountVolumesOriginalTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalMountVolumesOriginalTargetConfig from a JSON string
physical_mount_volumes_original_target_config_instance = PhysicalMountVolumesOriginalTargetConfig.from_json(json)
# print the JSON string representation of the object
print(PhysicalMountVolumesOriginalTargetConfig.to_json())

# convert the object into a dict
physical_mount_volumes_original_target_config_dict = physical_mount_volumes_original_target_config_instance.to_dict()
# create an instance of PhysicalMountVolumesOriginalTargetConfig from a dict
physical_mount_volumes_original_target_config_from_dict = PhysicalMountVolumesOriginalTargetConfig.from_dict(physical_mount_volumes_original_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


