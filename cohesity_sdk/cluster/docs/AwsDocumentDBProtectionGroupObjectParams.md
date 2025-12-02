# AwsDocumentDBProtectionGroupObjectParams

Specifies the object parameters to create an AWS DocumentDB Ingest Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the virtual machine. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_document_db_protection_group_object_params import AwsDocumentDBProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDocumentDBProtectionGroupObjectParams from a JSON string
aws_document_db_protection_group_object_params_instance = AwsDocumentDBProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsDocumentDBProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_document_db_protection_group_object_params_dict = aws_document_db_protection_group_object_params_instance.to_dict()
# create an instance of AwsDocumentDBProtectionGroupObjectParams from a dict
aws_document_db_protection_group_object_params_from_dict = AwsDocumentDBProtectionGroupObjectParams.from_dict(aws_document_db_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


