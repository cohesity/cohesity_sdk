# TieringAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies bucket name of the External Target. | 
**region** | **str** | Specifies region of the External Target. | 
**storage_class** | **str** | Specifies the AWS External Target storage class. | 
**aws_s3_intelligent_params** | [**AwsS3IntelligentParams**](AwsS3IntelligentParams.md) |  | [optional] 
**aws_s3_standard_params** | [**AwsS3StandardParams**](AwsS3StandardParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.tiering_aws_external_target_params import TieringAwsExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of TieringAwsExternalTargetParams from a JSON string
tiering_aws_external_target_params_instance = TieringAwsExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(TieringAwsExternalTargetParams.to_json())

# convert the object into a dict
tiering_aws_external_target_params_dict = tiering_aws_external_target_params_instance.to_dict()
# create an instance of TieringAwsExternalTargetParams from a dict
tiering_aws_external_target_params_from_dict = TieringAwsExternalTargetParams.from_dict(tiering_aws_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


