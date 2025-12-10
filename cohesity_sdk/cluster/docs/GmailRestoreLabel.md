# GmailRestoreLabel

Specifies a Gmail label or folder to recover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** | Specifies a list of item ids to recover. This field is applicable only if &#39;recoverEntireLabel&#39; is false. | [optional] 
**label_id** | **int** | Specifies the unique identifier of the label. | [optional] 
**label_name** | **str** | Specifies the name of the label. | [optional] 
**recover_entire_label** | **bool** | Specifies to recover all emails under this label. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gmail_restore_label import GmailRestoreLabel

# TODO update the JSON string below
json = "{}"
# create an instance of GmailRestoreLabel from a JSON string
gmail_restore_label_instance = GmailRestoreLabel.from_json(json)
# print the JSON string representation of the object
print(GmailRestoreLabel.to_json())

# convert the object into a dict
gmail_restore_label_dict = gmail_restore_label_instance.to_dict()
# create an instance of GmailRestoreLabel from a dict
gmail_restore_label_from_dict = GmailRestoreLabel.from_dict(gmail_restore_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


