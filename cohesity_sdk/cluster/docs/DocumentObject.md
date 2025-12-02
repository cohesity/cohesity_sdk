# DocumentObject

Specifies a document to download using item id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_directory** | **bool** | Specifies whether the document is a directory. Since currently only files are supported this should always be false. | [optional] 
**item_id** | **str** | Specifies the item id of the document. | 

## Example

```python
from cohesity_sdk.cluster.models.document_object import DocumentObject

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentObject from a JSON string
document_object_instance = DocumentObject.from_json(json)
# print the JSON string representation of the object
print(DocumentObject.to_json())

# convert the object into a dict
document_object_dict = document_object_instance.to_dict()
# create an instance of DocumentObject from a dict
document_object_from_dict = DocumentObject.from_dict(document_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


