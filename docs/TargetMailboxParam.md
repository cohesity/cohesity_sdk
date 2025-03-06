# TargetMailboxParam

Specifies the target Mailbox to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the target mailbox. Atleast one of id or primarySMTPAddress need to be defined. In case both id and primarySMTPAddress are defined then id takes precedence. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**parent_source_id** | **int** | Specifies the id of the domain for alternate domain recovery. | [optional] 
**primary_smtp_address** | **str** | Specifies the primary SMTP address of the target mailbox. Atleast one of id or primarySMTPAddress needs to be defined. In case both id and primarySMTPAddress are defined then id takes precedence. | [optional] 
**target_folder_path** | **str** | Specifies the path to the target folder. | 

## Example

```python
from cohesity_sdk.cluster.models.target_mailbox_param import TargetMailboxParam

# TODO update the JSON string below
json = "{}"
# create an instance of TargetMailboxParam from a JSON string
target_mailbox_param_instance = TargetMailboxParam.from_json(json)
# print the JSON string representation of the object
print(TargetMailboxParam.to_json())

# convert the object into a dict
target_mailbox_param_dict = target_mailbox_param_instance.to_dict()
# create an instance of TargetMailboxParam from a dict
target_mailbox_param_from_dict = TargetMailboxParam.from_dict(target_mailbox_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


