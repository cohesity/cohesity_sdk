# O365RestoreExclusionPolicy

Specifies the filter policy to be applied for exclusions in Microsoft 365 restores.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_item_policy** | [**CommonO365RestoreExclusionPolicy**](CommonO365RestoreExclusionPolicy.md) |  | [optional] 
**contact_item_policy** | [**CommonO365RestoreExclusionPolicy**](CommonO365RestoreExclusionPolicy.md) |  | [optional] 
**mail_item_policy** | [**CommonO365RestoreExclusionPolicy**](CommonO365RestoreExclusionPolicy.md) |  | [optional] 
**note_item_policy** | [**CommonO365RestoreExclusionPolicy**](CommonO365RestoreExclusionPolicy.md) |  | [optional] 
**task_item_policy** | [**CommonO365RestoreExclusionPolicy**](CommonO365RestoreExclusionPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.o365_restore_exclusion_policy import O365RestoreExclusionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of O365RestoreExclusionPolicy from a JSON string
o365_restore_exclusion_policy_instance = O365RestoreExclusionPolicy.from_json(json)
# print the JSON string representation of the object
print(O365RestoreExclusionPolicy.to_json())

# convert the object into a dict
o365_restore_exclusion_policy_dict = o365_restore_exclusion_policy_instance.to_dict()
# create an instance of O365RestoreExclusionPolicy from a dict
o365_restore_exclusion_policy_from_dict = O365RestoreExclusionPolicy.from_dict(o365_restore_exclusion_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


