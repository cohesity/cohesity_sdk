# AwsDocumentDBProtectionGroupParams

Specifies the parameters which are specific to AWS DocumentDB related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_db_tag_ids** | **List[List[int]]** | Array of arrays of Tag Ids that Specify db clusters to Protect. | [optional] 
**exclude_document_db_tag_ids** | **List[List[int]]** | Array of arrays of Tag Ids that Specify db clusters to Exclude. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[AwsDocumentDBProtectionGroupObjectParams]**](AwsDocumentDBProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_document_db_protection_group_params import AwsDocumentDBProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsDocumentDBProtectionGroupParams from a JSON string
aws_document_db_protection_group_params_instance = AwsDocumentDBProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AwsDocumentDBProtectionGroupParams.to_json())

# convert the object into a dict
aws_document_db_protection_group_params_dict = aws_document_db_protection_group_params_instance.to_dict()
# create an instance of AwsDocumentDBProtectionGroupParams from a dict
aws_document_db_protection_group_params_from_dict = AwsDocumentDBProtectionGroupParams.from_dict(aws_document_db_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


