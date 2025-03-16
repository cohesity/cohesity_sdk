# McmLastRunStatusStats

Specifies the last run's status and count of objects having that status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of objects having this status. | [optional] 
**status** | **str** | Specifies the status of last run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_last_run_status_stats import McmLastRunStatusStats

# TODO update the JSON string below
json = "{}"
# create an instance of McmLastRunStatusStats from a JSON string
mcm_last_run_status_stats_instance = McmLastRunStatusStats.from_json(json)
# print the JSON string representation of the object
print(McmLastRunStatusStats.to_json())

# convert the object into a dict
mcm_last_run_status_stats_dict = mcm_last_run_status_stats_instance.to_dict()
# create an instance of McmLastRunStatusStats from a dict
mcm_last_run_status_stats_from_dict = McmLastRunStatusStats.from_dict(mcm_last_run_status_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


