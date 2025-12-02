# CommonTieringAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets of tiering purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies bucket name of the External Target. | 
**region** | **str** | Specifies region of the External Target. | 
**storage_class** | **str** | Specifies the AWS External Target storage class. | 

## Example

```python
from cohesity_sdk.cluster.models.common_tiering_aws_external_target_params import CommonTieringAwsExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonTieringAwsExternalTargetParams from a JSON string
common_tiering_aws_external_target_params_instance = CommonTieringAwsExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonTieringAwsExternalTargetParams.to_json())

# convert the object into a dict
common_tiering_aws_external_target_params_dict = common_tiering_aws_external_target_params_instance.to_dict()
# create an instance of CommonTieringAwsExternalTargetParams from a dict
common_tiering_aws_external_target_params_from_dict = CommonTieringAwsExternalTargetParams.from_dict(common_tiering_aws_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


