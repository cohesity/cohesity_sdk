# O365DocumentMetadata

Specifies additional info needed for o365 recovery/download.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subsite_item** | [**SubsiteItem**](SubsiteItem.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.o365_document_metadata import O365DocumentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of O365DocumentMetadata from a JSON string
o365_document_metadata_instance = O365DocumentMetadata.from_json(json)
# print the JSON string representation of the object
print(O365DocumentMetadata.to_json())

# convert the object into a dict
o365_document_metadata_dict = o365_document_metadata_instance.to_dict()
# create an instance of O365DocumentMetadata from a dict
o365_document_metadata_from_dict = O365DocumentMetadata.from_dict(o365_document_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


