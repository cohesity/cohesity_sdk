# ViewsStats

Specifies a list of View stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**views_stats** | [**List[ViewStatsInfo]**](ViewStatsInfo.md) | Specifies a list of View stats. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.views_stats import ViewsStats

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsStats from a JSON string
views_stats_instance = ViewsStats.from_json(json)
# print the JSON string representation of the object
print(ViewsStats.to_json())

# convert the object into a dict
views_stats_dict = views_stats_instance.to_dict()
# create an instance of ViewsStats from a dict
views_stats_from_dict = ViewsStats.from_dict(views_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


