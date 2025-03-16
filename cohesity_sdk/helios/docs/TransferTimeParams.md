# TransferTimeParams

Transfer time configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **List[str]** | List of days of a week. | 
**end_time** | [**TransferTimeOfDay**](TransferTimeOfDay.md) |  | 
**start_time** | [**TransferTimeOfDay**](TransferTimeOfDay.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_params import TransferTimeParams

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeParams from a JSON string
transfer_time_params_instance = TransferTimeParams.from_json(json)
# print the JSON string representation of the object
print(TransferTimeParams.to_json())

# convert the object into a dict
transfer_time_params_dict = transfer_time_params_instance.to_dict()
# create an instance of TransferTimeParams from a dict
transfer_time_params_from_dict = TransferTimeParams.from_dict(transfer_time_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


