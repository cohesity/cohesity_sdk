# FilerLifecycleAgingPolicy

Specifies the aging policy. Note: Both the fields days and dateInUsecs are mutually exclusive to each other.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aging_criteria** | **str** | Specifies the criteria for aging | 
**date_in_usecs** | **int** | Files that possess timestamps exceeding the specified value will be eligible for selection. | [optional] 
**days** | **int** | Files that possess timestamps older than the specified value in days will be eligible for selection. | [optional] 

## Example

```python
from cohesity_sdk.models.filer_lifecycle_aging_policy import FilerLifecycleAgingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FilerLifecycleAgingPolicy from a JSON string
filer_lifecycle_aging_policy_instance = FilerLifecycleAgingPolicy.from_json(json)
# print the JSON string representation of the object
print(FilerLifecycleAgingPolicy.to_json())

# convert the object into a dict
filer_lifecycle_aging_policy_dict = filer_lifecycle_aging_policy_instance.to_dict()
# create an instance of FilerLifecycleAgingPolicy from a dict
filer_lifecycle_aging_policy_from_dict = FilerLifecycleAgingPolicy.from_dict(filer_lifecycle_aging_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


