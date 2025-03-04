# ObjectMailboxParam

Specifies Mailbox recovery parameters associated with a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox_params** | [**MailboxParam**](MailboxParam.md) |  | 
**owner_info** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | 

## Example

```python
from cohesity_sdk.models.object_mailbox_param import ObjectMailboxParam

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMailboxParam from a JSON string
object_mailbox_param_instance = ObjectMailboxParam.from_json(json)
# print the JSON string representation of the object
print(ObjectMailboxParam.to_json())

# convert the object into a dict
object_mailbox_param_dict = object_mailbox_param_instance.to_dict()
# create an instance of ObjectMailboxParam from a dict
object_mailbox_param_from_dict = ObjectMailboxParam.from_dict(object_mailbox_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


