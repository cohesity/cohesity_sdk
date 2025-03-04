# AwsSourceRegistrationParams

Specifies the paramaters to register an AWS source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_params** | [**S3SpecificParams**](S3SpecificParams.md) |  | [optional] 
**standard_params** | [**StandardParams**](StandardParams.md) |  | [optional] 
**subscription_type** | **str** | Specifies the AWS Subscription type (Commercial/Gov). | 

## Example

```python
from cohesity_sdk.models.aws_source_registration_params import AwsSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSourceRegistrationParams from a JSON string
aws_source_registration_params_instance = AwsSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(AwsSourceRegistrationParams.to_json())

# convert the object into a dict
aws_source_registration_params_dict = aws_source_registration_params_instance.to_dict()
# create an instance of AwsSourceRegistrationParams from a dict
aws_source_registration_params_from_dict = AwsSourceRegistrationParams.from_dict(aws_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


