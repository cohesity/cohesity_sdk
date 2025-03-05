# MailboxParam

Specifies parameters to recover a Mailbox.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_entire_mailbox** | **bool** | Specifies whether to recover the whole Mailbox. | [optional] 
**recover_folders** | [**List[FolderItem]**](FolderItem.md) | Specifies a list of email folders to recover. | [optional] 

## Example

```python
from cohesity_sdk.models.mailbox_param import MailboxParam

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxParam from a JSON string
mailbox_param_instance = MailboxParam.from_json(json)
# print the JSON string representation of the object
print(MailboxParam.to_json())

# convert the object into a dict
mailbox_param_dict = mailbox_param_instance.to_dict()
# create an instance of MailboxParam from a dict
mailbox_param_from_dict = MailboxParam.from_dict(mailbox_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


