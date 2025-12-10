# FortknoxOnpremVaultingActivities

Specifies the Fortknox Onprem vaulting replication run activities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activities** | [**List[FortknoxOnpremVaultingActivity]**](FortknoxOnpremVaultingActivity.md) | Specifies the vaulting replication run activity list. | [optional] 
**pagination_cookie** | **str** | Specifies the information needed in order to support pagination. This will not be included for the last page of results. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.fortknox_onprem_vaulting_activities import FortknoxOnpremVaultingActivities

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxOnpremVaultingActivities from a JSON string
fortknox_onprem_vaulting_activities_instance = FortknoxOnpremVaultingActivities.from_json(json)
# print the JSON string representation of the object
print(FortknoxOnpremVaultingActivities.to_json())

# convert the object into a dict
fortknox_onprem_vaulting_activities_dict = fortknox_onprem_vaulting_activities_instance.to_dict()
# create an instance of FortknoxOnpremVaultingActivities from a dict
fortknox_onprem_vaulting_activities_from_dict = FortknoxOnpremVaultingActivities.from_dict(fortknox_onprem_vaulting_activities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


