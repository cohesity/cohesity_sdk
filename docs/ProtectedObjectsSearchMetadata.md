# ProtectedObjectsSearchMetadata

Specifies the metadata information about the Protection Groups, Protection Policy etc., for search result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_protection_group_identifiers** | [**List[ProtectionGroupIdentifier]**](ProtectionGroupIdentifier.md) | Specifies the list of unique Protection Group identifiers for all the Objects returned in the response. | [optional] 

## Example

```python
from cohesity_sdk.models.protected_objects_search_metadata import ProtectedObjectsSearchMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectsSearchMetadata from a JSON string
protected_objects_search_metadata_instance = ProtectedObjectsSearchMetadata.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectsSearchMetadata.to_json())

# convert the object into a dict
protected_objects_search_metadata_dict = protected_objects_search_metadata_instance.to_dict()
# create an instance of ProtectedObjectsSearchMetadata from a dict
protected_objects_search_metadata_from_dict = ProtectedObjectsSearchMetadata.from_dict(protected_objects_search_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


