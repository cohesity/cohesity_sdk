# TransferTimeConfigurationParams

Transfer time configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[str]** | List of days of a week. | 
**end_time** | [**TransferTimeOfTheDay**](TransferTimeOfTheDay.md) |  | 
**start_time** | [**TransferTimeOfTheDay**](TransferTimeOfTheDay.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_configuration_params import TransferTimeConfigurationParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeConfigurationParams from a JSON string
transfer_time_configuration_params_instance = TransferTimeConfigurationParams.from_json(json)
# print the JSON string representation of the object
print(TransferTimeConfigurationParams.to_json())

# convert the object into a dict
transfer_time_configuration_params_dict = transfer_time_configuration_params_instance.to_dict()
# create an instance of TransferTimeConfigurationParams from a dict
transfer_time_configuration_params_from_dict = TransferTimeConfigurationParams.from_dict(transfer_time_configuration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


