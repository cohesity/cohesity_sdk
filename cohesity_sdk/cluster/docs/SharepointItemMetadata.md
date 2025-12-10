# SharepointItemMetadata

Info about a sharepoint item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of the sharepoint item | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.sharepoint_item_metadata import SharepointItemMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointItemMetadata from a JSON string
sharepoint_item_metadata_instance = SharepointItemMetadata.from_json(json)
# print the JSON string representation of the object
print(SharepointItemMetadata.to_json())

# convert the object into a dict
sharepoint_item_metadata_dict = sharepoint_item_metadata_instance.to_dict()
# create an instance of SharepointItemMetadata from a dict
sharepoint_item_metadata_from_dict = SharepointItemMetadata.from_dict(sharepoint_item_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


