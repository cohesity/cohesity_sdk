# TransferTimeConfigParamsList

Transfer time configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone for the transfer time periods. | [optional] [default to 'America/Los_Angeles']
**transfer_times** | [**List[TransferTimeConfigurationParams]**](TransferTimeConfigurationParams.md) | List of transfer time configurations. | 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_config_params_list import TransferTimeConfigParamsList

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeConfigParamsList from a JSON string
transfer_time_config_params_list_instance = TransferTimeConfigParamsList.from_json(json)
# print the JSON string representation of the object
print(TransferTimeConfigParamsList.to_json())

# convert the object into a dict
transfer_time_config_params_list_dict = transfer_time_config_params_list_instance.to_dict()
# create an instance of TransferTimeConfigParamsList from a dict
transfer_time_config_params_list_from_dict = TransferTimeConfigParamsList.from_dict(transfer_time_config_params_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


