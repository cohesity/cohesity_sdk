# MsGroupParam

Specifies parameters to recover MS group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_restore_params** | [**MailboxParam**](MailboxParam.md) |  | [optional] 
**mailbox_restore_type** | **str** | Specifies whether mailbox restore is full or granular. | [optional] 
**recover_entire_group** | **bool** | Specifies if the entire Group (mailbox + site) is to be restored. | [optional] 
**recover_object** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | 
**site_restore_params** | [**List[OneDriveParam]**](OneDriveParam.md) | Specifies the parameters to recover a MSGroup site document. | [optional] 
**site_restore_type** | **str** | Specifies whether site restore is full or granular. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ms_group_param import MsGroupParam

# TODO update the JSON string below
json = "{}"
# create an instance of MsGroupParam from a JSON string
ms_group_param_instance = MsGroupParam.from_json(json)
# print the JSON string representation of the object
print(MsGroupParam.to_json())

# convert the object into a dict
ms_group_param_dict = ms_group_param_instance.to_dict()
# create an instance of MsGroupParam from a dict
ms_group_param_from_dict = MsGroupParam.from_dict(ms_group_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


