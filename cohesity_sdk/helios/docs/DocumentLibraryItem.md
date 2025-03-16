# DocumentLibraryItem

Specifies a Document Library indexed item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the object. | [optional] 
**path** | **str** | Specifies the path of the object. | [optional] 
**policy_id** | **str** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | **object** | Specifies the Source Object information. | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**creation_time_secs** | **int** | Specifies the Unix timestamp epoch in seconds at which this item is created. | [optional] 
**file_type** | **str** | Specifies the file type. | [optional] 
**item_size** | **int** | Specifies the size in bytes for the indexed item. | [optional] 
**owner_email** | **str** | Specifies the email of the owner of the document library item. | [optional] 
**owner_name** | **str** | Specifies the name of the owner of the document library item. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.document_library_item import DocumentLibraryItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentLibraryItem from a JSON string
document_library_item_instance = DocumentLibraryItem.from_json(json)
# print the JSON string representation of the object
print(DocumentLibraryItem.to_json())

# convert the object into a dict
document_library_item_dict = document_library_item_instance.to_dict()
# create an instance of DocumentLibraryItem from a dict
document_library_item_from_dict = DocumentLibraryItem.from_dict(document_library_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


