# StandardParams

Specifies the parameters to register a commercial AWS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_method_type** | **str** | Specifies the Authentication method(IamArn/IamRole) used by api | 
**iam_role_aws_credentials** | [**IamRoleAwsCredentials**](IamRoleAwsCredentials.md) |  | [optional] 
**iam_user_aws_credentials** | [**IamUserAwsCredentials**](IamUserAwsCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.standard_params import StandardParams

# TODO update the JSON string below
json = "{}"
# create an instance of StandardParams from a JSON string
standard_params_instance = StandardParams.from_json(json)
# print the JSON string representation of the object
print(StandardParams.to_json())

# convert the object into a dict
standard_params_dict = standard_params_instance.to_dict()
# create an instance of StandardParams from a dict
standard_params_from_dict = StandardParams.from_dict(standard_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


