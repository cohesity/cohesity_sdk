# UpdateProtectionGroupsState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_protection_groups** | [**List[FailedProtectionGroupDetails]**](FailedProtectionGroupDetails.md) | Specifies a list of Protection Group ids along with details for which updation of state was failed. | [optional] 
**successful_protection_group_ids** | **List[str]** | Specifies a list of Protection Group ids for which updation of state was successful. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_protection_groups_state import UpdateProtectionGroupsState

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProtectionGroupsState from a JSON string
update_protection_groups_state_instance = UpdateProtectionGroupsState.from_json(json)
# print the JSON string representation of the object
print(UpdateProtectionGroupsState.to_json())

# convert the object into a dict
update_protection_groups_state_dict = update_protection_groups_state_instance.to_dict()
# create an instance of UpdateProtectionGroupsState from a dict
update_protection_groups_state_from_dict = UpdateProtectionGroupsState.from_dict(update_protection_groups_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


