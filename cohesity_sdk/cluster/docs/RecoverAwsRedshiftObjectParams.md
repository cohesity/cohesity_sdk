# RecoverAwsRedshiftObjectParams

Specifies details of recovery object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str** | The Cloud Storage bucket name for Redshift backup. | [optional] 
**new_name** | **str** | Specifies the new name to which the object should be renamed to after the recovery. | [optional] 
**original_name** | **str** | Specifies the original name of the object to be restored, as it exists in the source. | [optional] 
**overwrite** | **bool** | Specifies whether to overwrite an existing object with the same name at the destination. If true, any existing object will be replaced; if false or unset, the restore may fail if a conflict occurs. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_redshift_object_params import RecoverAwsRedshiftObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRedshiftObjectParams from a JSON string
recover_aws_redshift_object_params_instance = RecoverAwsRedshiftObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRedshiftObjectParams.to_json())

# convert the object into a dict
recover_aws_redshift_object_params_dict = recover_aws_redshift_object_params_instance.to_dict()
# create an instance of RecoverAwsRedshiftObjectParams from a dict
recover_aws_redshift_object_params_from_dict = RecoverAwsRedshiftObjectParams.from_dict(recover_aws_redshift_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


