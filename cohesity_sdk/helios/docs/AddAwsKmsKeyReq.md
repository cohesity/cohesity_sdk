# AddAwsKmsKeyReq

Request about the KMS key provisioned in AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kms_key_arn** | **str** | ARN of the KMS key. This is required for customer managed key. | [optional] 
**region_id** | **str** | ID that identifies a region of the KMS key. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_aws_kms_key_req import AddAwsKmsKeyReq

# TODO update the JSON string below
json = "{}"
# create an instance of AddAwsKmsKeyReq from a JSON string
add_aws_kms_key_req_instance = AddAwsKmsKeyReq.from_json(json)
# print the JSON string representation of the object
print(AddAwsKmsKeyReq.to_json())

# convert the object into a dict
add_aws_kms_key_req_dict = add_aws_kms_key_req_instance.to_dict()
# create an instance of AddAwsKmsKeyReq from a dict
add_aws_kms_key_req_from_dict = AddAwsKmsKeyReq.from_dict(add_aws_kms_key_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


