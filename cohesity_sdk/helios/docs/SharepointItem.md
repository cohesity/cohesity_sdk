# SharepointItem

Specifies the indexed Sharepoint item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_library_item** | [**DocumentLibraryItem**](DocumentLibraryItem.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.sharepoint_item import SharepointItem

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointItem from a JSON string
sharepoint_item_instance = SharepointItem.from_json(json)
# print the JSON string representation of the object
print(SharepointItem.to_json())

# convert the object into a dict
sharepoint_item_dict = sharepoint_item_instance.to_dict()
# create an instance of SharepointItem from a dict
sharepoint_item_from_dict = SharepointItem.from_dict(sharepoint_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


