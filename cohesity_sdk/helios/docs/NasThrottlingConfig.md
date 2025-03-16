# NasThrottlingConfig

Specifies the source throttling parameters to be used during full or incremental backup of the NAS source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_backup_config** | [**NasFullThrottlingConfig**](NasFullThrottlingConfig.md) |  | [optional] 
**incremental_backup_config** | [**NasIncrementalThrottlingConfig**](NasIncrementalThrottlingConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.nas_throttling_config import NasThrottlingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NasThrottlingConfig from a JSON string
nas_throttling_config_instance = NasThrottlingConfig.from_json(json)
# print the JSON string representation of the object
print(NasThrottlingConfig.to_json())

# convert the object into a dict
nas_throttling_config_dict = nas_throttling_config_instance.to_dict()
# create an instance of NasThrottlingConfig from a dict
nas_throttling_config_from_dict = NasThrottlingConfig.from_dict(nas_throttling_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


