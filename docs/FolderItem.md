# FolderItem

Specifies an email folder to recover.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ids** | **List[str]** | Specifies a list of item ids to recover. This field is applicable only if &#39;recoverEntireFolder&#39; is false. | [optional] 
**key** | **int** | Specifies the email folder key. | 
**recover_entire_folder** | **bool** | Specifies whether to recover the whole email folder. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.folder_item import FolderItem

# TODO update the JSON string below
json = "{}"
# create an instance of FolderItem from a JSON string
folder_item_instance = FolderItem.from_json(json)
# print the JSON string representation of the object
print(FolderItem.to_json())

# convert the object into a dict
folder_item_dict = folder_item_instance.to_dict()
# create an instance of FolderItem from a dict
folder_item_from_dict = FolderItem.from_dict(folder_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


