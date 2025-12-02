# AwsDocumentDBMetadata

Specifies the metadata types and values of aws documentdb.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** | Specifies the type of metadata being sent in the request. | 
**standard_credentials** | [**AwsCredentials**](AwsCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_document_db_metadata import AwsDocumentDBMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDocumentDBMetadata from a JSON string
aws_document_db_metadata_instance = AwsDocumentDBMetadata.from_json(json)
# print the JSON string representation of the object
print(AwsDocumentDBMetadata.to_json())

# convert the object into a dict
aws_document_db_metadata_dict = aws_document_db_metadata_instance.to_dict()
# create an instance of AwsDocumentDBMetadata from a dict
aws_document_db_metadata_from_dict = AwsDocumentDBMetadata.from_dict(aws_document_db_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


