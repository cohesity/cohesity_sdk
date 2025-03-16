# ProtectionRunsStatsList

Specifies the statistics of protection runs at the specific time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**List[ProtectionRunsStats]**](ProtectionRunsStats.md) | Specifies the protection runs stats. | [optional] 
**timestamp** | **int** | Specifies a Unix epoch Timestamp (in microseconds) of this statistics. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_runs_stats_list import ProtectionRunsStatsList

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionRunsStatsList from a JSON string
protection_runs_stats_list_instance = ProtectionRunsStatsList.from_json(json)
# print the JSON string representation of the object
print(ProtectionRunsStatsList.to_json())

# convert the object into a dict
protection_runs_stats_list_dict = protection_runs_stats_list_instance.to_dict()
# create an instance of ProtectionRunsStatsList from a dict
protection_runs_stats_list_from_dict = ProtectionRunsStatsList.from_dict(protection_runs_stats_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


