# RecoverMailboxParams

Specifies the parameters to recover an Office 365 Mailbox.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other Mailboxes if one of Mailbox failed to recover. Default value is false. | [optional] 
**objects** | [**List[ObjectMailboxParam]**](ObjectMailboxParam.md) | Specifies a list of Mailbox params associated with the objects to recover. | 
**pst_params** | [**PstParam**](PstParam.md) |  | [optional] 
**skip_recover_archive_mailbox** | **bool** | Specifies whether to skip the recovery of the archive mailbox and/or items present in the archive mailbox. Default value is true | [optional] 
**skip_recover_archive_recoverable_items** | **bool** | Specifies whether to skip the recovery of the Archive Recoverable Items present in the selected snapshot. Default value is true | [optional] 
**skip_recover_recoverable_items** | **bool** | Specifies whether to skip the recovery of the Recoverable Items present in the selected snapshot. Default value is true | [optional] 
**target_mailbox** | [**TargetMailboxParam**](TargetMailboxParam.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_mailbox_params import RecoverMailboxParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverMailboxParams from a JSON string
recover_mailbox_params_instance = RecoverMailboxParams.from_json(json)
# print the JSON string representation of the object
print(RecoverMailboxParams.to_json())

# convert the object into a dict
recover_mailbox_params_dict = recover_mailbox_params_instance.to_dict()
# create an instance of RecoverMailboxParams from a dict
recover_mailbox_params_from_dict = RecoverMailboxParams.from_dict(recover_mailbox_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


