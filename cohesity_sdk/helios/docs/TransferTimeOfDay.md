# TransferTimeOfDay

Transfer time of the day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | Specifies the hour of the day (0-23). | 
**minute** | **int** | Specifies the minute of the hour (0-59). | 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_of_day import TransferTimeOfDay

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeOfDay from a JSON string
transfer_time_of_day_instance = TransferTimeOfDay.from_json(json)
# print the JSON string representation of the object
print(TransferTimeOfDay.to_json())

# convert the object into a dict
transfer_time_of_day_dict = transfer_time_of_day_instance.to_dict()
# create an instance of TransferTimeOfDay from a dict
transfer_time_of_day_from_dict = TransferTimeOfDay.from_dict(transfer_time_of_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


