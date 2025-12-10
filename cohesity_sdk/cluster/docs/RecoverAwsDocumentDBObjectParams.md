# RecoverAwsDocumentDBObjectParams

Specifies details of DocumentDB recovery object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** | Specifies the new name to which the DocumentDB cluster should be renamed to after the recovery. | [optional] 
**original_name** | **str** | Specifies the original name of the DocumentDB cluster to be restored, as it exists in the source. | [optional] 
**overwrite** | **bool** | Specifies whether to overwrite an existing DocumentDB cluster with the same name at the destination. If true, any existing cluster will be replaced; if false or unset, the restore may fail if a conflict occurs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_document_db_object_params import RecoverAwsDocumentDBObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsDocumentDBObjectParams from a JSON string
recover_aws_document_db_object_params_instance = RecoverAwsDocumentDBObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsDocumentDBObjectParams.to_json())

# convert the object into a dict
recover_aws_document_db_object_params_dict = recover_aws_document_db_object_params_instance.to_dict()
# create an instance of RecoverAwsDocumentDBObjectParams from a dict
recover_aws_document_db_object_params_from_dict = RecoverAwsDocumentDBObjectParams.from_dict(recover_aws_document_db_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


