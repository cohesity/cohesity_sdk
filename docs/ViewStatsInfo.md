# ViewStatsInfo

Specifies the View stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocols** | **List[str]** | Specifies the protocols of this view. | [optional] 
**stats** | [**List[ViewStatsInfoDetails]**](ViewStatsInfoDetails.md) | Specifies the list of View stats. | [optional] 
**view_id** | **int** | Specifies the view Id. | [optional] 
**view_name** | **str** | Specifies the view name. | [optional] 

## Example

```python
from cohesity_sdk.models.view_stats_info import ViewStatsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ViewStatsInfo from a JSON string
view_stats_info_instance = ViewStatsInfo.from_json(json)
# print the JSON string representation of the object
print(ViewStatsInfo.to_json())

# convert the object into a dict
view_stats_info_dict = view_stats_info_instance.to_dict()
# create an instance of ViewStatsInfo from a dict
view_stats_info_from_dict = ViewStatsInfo.from_dict(view_stats_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


