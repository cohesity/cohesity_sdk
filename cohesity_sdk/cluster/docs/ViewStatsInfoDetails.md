# ViewStatsInfoDetails

Specifies the View stats details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** | Specifies the stats metric. | [optional] 
**value_in_last_hours** | [**List[ViewStatsInLastHours]**](ViewStatsInLastHours.md) | Specifies the stats value in last hours. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_stats_info_details import ViewStatsInfoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ViewStatsInfoDetails from a JSON string
view_stats_info_details_instance = ViewStatsInfoDetails.from_json(json)
# print the JSON string representation of the object
print(ViewStatsInfoDetails.to_json())

# convert the object into a dict
view_stats_info_details_dict = view_stats_info_details_instance.to_dict()
# create an instance of ViewStatsInfoDetails from a dict
view_stats_info_details_from_dict = ViewStatsInfoDetails.from_dict(view_stats_info_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


