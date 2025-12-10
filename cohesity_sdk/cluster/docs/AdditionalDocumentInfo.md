# AdditionalDocumentInfo

Specifies additional info needed for o365 recovery/download.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o365_params** | [**O365DocumentMetadata**](O365DocumentMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.additional_document_info import AdditionalDocumentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalDocumentInfo from a JSON string
additional_document_info_instance = AdditionalDocumentInfo.from_json(json)
# print the JSON string representation of the object
print(AdditionalDocumentInfo.to_json())

# convert the object into a dict
additional_document_info_dict = additional_document_info_instance.to_dict()
# create an instance of AdditionalDocumentInfo from a dict
additional_document_info_from_dict = AdditionalDocumentInfo.from_dict(additional_document_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


