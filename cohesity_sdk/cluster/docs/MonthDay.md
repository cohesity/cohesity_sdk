# MonthDay

Specificies the date and time information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_the_month** | **int** | Indicates day of the month. | [optional] 
**month** | **int** | Indicates month for specific date. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.month_day import MonthDay

# TODO update the JSON string below
json = "{}"
# create an instance of MonthDay from a JSON string
month_day_instance = MonthDay.from_json(json)
# print the JSON string representation of the object
print(MonthDay.to_json())

# convert the object into a dict
month_day_dict = month_day_instance.to_dict()
# create an instance of MonthDay from a dict
month_day_from_dict = MonthDay.from_dict(month_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


