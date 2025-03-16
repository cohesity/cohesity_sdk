# ProtectionGroups

Protection Group  response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_cookie** | **str** | Specifies the information needed in order to support pagination. This will not be included for the last page of results. | [optional] 
**protection_groups** | [**List[ProtectionGroup]**](ProtectionGroup.md) | Specifies the list of Protection Groups which were returned by the request. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protection_groups import ProtectionGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroups from a JSON string
protection_groups_instance = ProtectionGroups.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroups.to_json())

# convert the object into a dict
protection_groups_dict = protection_groups_instance.to_dict()
# create an instance of ProtectionGroups from a dict
protection_groups_from_dict = ProtectionGroups.from_dict(protection_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


