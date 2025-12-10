# VaultingWindowConfig

Vaulting window configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone for the vaulting windows. | [optional] [default to 'America/Los_Angeles']
**vaulting_windows** | [**List[VaultingWindowParams]**](VaultingWindowParams.md) | List of vaulting window params. | 

## Example

```python
from cohesity_sdk.cluster.models.vaulting_window_config import VaultingWindowConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VaultingWindowConfig from a JSON string
vaulting_window_config_instance = VaultingWindowConfig.from_json(json)
# print the JSON string representation of the object
print(VaultingWindowConfig.to_json())

# convert the object into a dict
vaulting_window_config_dict = vaulting_window_config_instance.to_dict()
# create an instance of VaultingWindowConfig from a dict
vaulting_window_config_from_dict = VaultingWindowConfig.from_dict(vaulting_window_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


