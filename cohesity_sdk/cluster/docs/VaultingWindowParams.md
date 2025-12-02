# VaultingWindowParams

Transfer time configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[str]** | List of days of a week. | 
**end_time** | [**VaultingTimeOfTheDay**](VaultingTimeOfTheDay.md) |  | 
**start_time** | [**VaultingTimeOfTheDay**](VaultingTimeOfTheDay.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.vaulting_window_params import VaultingWindowParams

# TODO update the JSON string below
json = "{}"
# create an instance of VaultingWindowParams from a JSON string
vaulting_window_params_instance = VaultingWindowParams.from_json(json)
# print the JSON string representation of the object
print(VaultingWindowParams.to_json())

# convert the object into a dict
vaulting_window_params_dict = vaulting_window_params_instance.to_dict()
# create an instance of VaultingWindowParams from a dict
vaulting_window_params_from_dict = VaultingWindowParams.from_dict(vaulting_window_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


