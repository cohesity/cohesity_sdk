# UserOtpParams

Specifies the parameters to verify User OTP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | Specifies the OTP provided from the user. | 
**otp_type** | **str** | Specifies OTP type. | 

## Example

```python
from cohesity_sdk.cluster.models.user_otp_params import UserOtpParams

# TODO update the JSON string below
json = "{}"
# create an instance of UserOtpParams from a JSON string
user_otp_params_instance = UserOtpParams.from_json(json)
# print the JSON string representation of the object
print(UserOtpParams.to_json())

# convert the object into a dict
user_otp_params_dict = user_otp_params_instance.to_dict()
# create an instance of UserOtpParams from a dict
user_otp_params_from_dict = UserOtpParams.from_dict(user_otp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


