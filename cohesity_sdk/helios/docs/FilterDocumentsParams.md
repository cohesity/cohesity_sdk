# FilterDocumentsParams

Specifies the parameters to filter documents to be restored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_filter_type** | **str** | Specifies the filter type for Documents to be restored. | 
**filter_expression** | **str** | A filter expression to match Documents content to be restored. | [optional] 
**id_regex** | **str** | A regular expression to match Documents ID&#39;s to be restored. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.filter_documents_params import FilterDocumentsParams

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDocumentsParams from a JSON string
filter_documents_params_instance = FilterDocumentsParams.from_json(json)
# print the JSON string representation of the object
print(FilterDocumentsParams.to_json())

# convert the object into a dict
filter_documents_params_dict = filter_documents_params_instance.to_dict()
# create an instance of FilterDocumentsParams from a dict
filter_documents_params_from_dict = FilterDocumentsParams.from_dict(filter_documents_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


