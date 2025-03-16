# TransferTimeConfigParams

Transfer time configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone for the transfer time periods. | [optional] [default to 'America/Los_Angeles']
**transfer_times** | [**List[TransferTimeParams]**](TransferTimeParams.md) | List of transfer time configurations. | 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_config_params import TransferTimeConfigParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeConfigParams from a JSON string
transfer_time_config_params_instance = TransferTimeConfigParams.from_json(json)
# print the JSON string representation of the object
print(TransferTimeConfigParams.to_json())

# convert the object into a dict
transfer_time_config_params_dict = transfer_time_config_params_instance.to_dict()
# create an instance of TransferTimeConfigParams from a dict
transfer_time_config_params_from_dict = TransferTimeConfigParams.from_dict(transfer_time_config_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


