# ViewStats

Provides statistics about the View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_usage_stats** | [**DataUsageStats**](DataUsageStats.md) | Specifies the data usage metric of the data stored in this View. | [optional] 
**id** | **int** | Specifies the id of the View. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_stats import ViewStats

# TODO update the JSON string below
json = "{}"
# create an instance of ViewStats from a JSON string
view_stats_instance = ViewStats.from_json(json)
# print the JSON string representation of the object
print(ViewStats.to_json())

# convert the object into a dict
view_stats_dict = view_stats_instance.to_dict()
# create an instance of ViewStats from a dict
view_stats_from_dict = ViewStats.from_dict(view_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


