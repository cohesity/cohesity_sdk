# CommonAwsExternalTargetParams

Specifies the common parameters which are specific to AWS related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Specifies bucket name of the External Target. | 
**region** | **str** | Specifies region of the External Target. | 

## Example

```python
from cohesity_sdk.models.common_aws_external_target_params import CommonAwsExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAwsExternalTargetParams from a JSON string
common_aws_external_target_params_instance = CommonAwsExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonAwsExternalTargetParams.to_json())

# convert the object into a dict
common_aws_external_target_params_dict = common_aws_external_target_params_instance.to_dict()
# create an instance of CommonAwsExternalTargetParams from a dict
common_aws_external_target_params_from_dict = CommonAwsExternalTargetParams.from_dict(common_aws_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


