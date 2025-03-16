# ActivityStatsParams

Specifies the parameters to fetch stats for object activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | Specifies the list of attributes to perform aggregations on. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.activity_stats_params import ActivityStatsParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStatsParams from a JSON string
activity_stats_params_instance = ActivityStatsParams.from_json(json)
# print the JSON string representation of the object
print(ActivityStatsParams.to_json())

# convert the object into a dict
activity_stats_params_dict = activity_stats_params_instance.to_dict()
# create an instance of ActivityStatsParams from a dict
activity_stats_params_from_dict = ActivityStatsParams.from_dict(activity_stats_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


