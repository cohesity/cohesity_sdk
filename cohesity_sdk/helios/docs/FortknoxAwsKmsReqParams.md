# FortknoxAwsKmsReqParams

Fortknox vault KMS related params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_arn** | **str** | ARN of the KMS key. This field is only applicable for customer managed KMS key. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.fortknox_aws_kms_req_params import FortknoxAwsKmsReqParams

# TODO update the JSON string below
json = "{}"
# create an instance of FortknoxAwsKmsReqParams from a JSON string
fortknox_aws_kms_req_params_instance = FortknoxAwsKmsReqParams.from_json(json)
# print the JSON string representation of the object
print(FortknoxAwsKmsReqParams.to_json())

# convert the object into a dict
fortknox_aws_kms_req_params_dict = fortknox_aws_kms_req_params_instance.to_dict()
# create an instance of FortknoxAwsKmsReqParams from a dict
fortknox_aws_kms_req_params_from_dict = FortknoxAwsKmsReqParams.from_dict(fortknox_aws_kms_req_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


