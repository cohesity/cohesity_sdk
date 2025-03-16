# TransferTimeOfTheDay

Transfer time configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | Specifies the hour of the day (0-23). | 
**minute** | **int** | Specifies the minute of the hour (0-59). | 

## Example

```python
from cohesity_sdk.helios.models.transfer_time_of_the_day import TransferTimeOfTheDay

# TODO update the JSON string below
json = "{}"
# create an instance of TransferTimeOfTheDay from a JSON string
transfer_time_of_the_day_instance = TransferTimeOfTheDay.from_json(json)
# print the JSON string representation of the object
print(TransferTimeOfTheDay.to_json())

# convert the object into a dict
transfer_time_of_the_day_dict = transfer_time_of_the_day_instance.to_dict()
# create an instance of TransferTimeOfTheDay from a dict
transfer_time_of_the_day_from_dict = TransferTimeOfTheDay.from_dict(transfer_time_of_the_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


