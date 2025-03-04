# ProtectionGroupRuns

Protection runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_cookie** | **str** | Specifies the information needed in order to support pagination. This will not be included for the last page of results. | [optional] 
**runs** | [**List[CommonProtectionGroupRunResponseParameters]**](CommonProtectionGroupRunResponseParameters.md) | Specifies the list of Protection Group runs. | [optional] 
**total_runs** | **int** | Specifies the count of total runs exist for the given set of filters. The number of runs in single API call are limited and this count can be used to estimate query filter values to get next set of remaining runs. Please note that this field will only be populated if startTimeUsecs or endTimeUsecs or both are specified in query parameters. | [optional] 

## Example

```python
from cohesity_sdk.models.protection_group_runs import ProtectionGroupRuns

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupRuns from a JSON string
protection_group_runs_instance = ProtectionGroupRuns.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupRuns.to_json())

# convert the object into a dict
protection_group_runs_dict = protection_group_runs_instance.to_dict()
# create an instance of ProtectionGroupRuns from a dict
protection_group_runs_from_dict = ProtectionGroupRuns.from_dict(protection_group_runs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


