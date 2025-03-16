# CommonS3CompExternalTargetParams

Specifies the common parameters which are specific to S3 Compatible related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Specifies the access key id of the external target. | 
**bucket_name** | **str** | Specifies the bucket name of the external target. | 
**end_point** | **str** | Specifies the endpoint of the external target. | 
**is_aws_snowball** | **bool** | Specifies whether the external target is AWS Snowball. | [optional] 
**region** | **str** | Specifies the region of the external target. | [optional] 
**secret_access_key** | **str** | Specifies the secret access key of the external target. | [optional] 
**secure_connection** | **bool** | Specifies the secure connection(https) is enabled or not. | [optional] 
**signature_version** | **int** | Specifies the aws signature version of the external target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_s3_comp_external_target_params import CommonS3CompExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonS3CompExternalTargetParams from a JSON string
common_s3_comp_external_target_params_instance = CommonS3CompExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonS3CompExternalTargetParams.to_json())

# convert the object into a dict
common_s3_comp_external_target_params_dict = common_s3_comp_external_target_params_instance.to_dict()
# create an instance of CommonS3CompExternalTargetParams from a dict
common_s3_comp_external_target_params_from_dict = CommonS3CompExternalTargetParams.from_dict(common_s3_comp_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


