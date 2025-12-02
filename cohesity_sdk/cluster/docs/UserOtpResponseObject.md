# UserOtpResponseObject

Returns a Boolean Indicating Status With User Details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Specifies whether the Operation Was Successful. | 
**user_details** | [**UserDetails**](UserDetails.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.user_otp_response_object import UserOtpResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of UserOtpResponseObject from a JSON string
user_otp_response_object_instance = UserOtpResponseObject.from_json(json)
# print the JSON string representation of the object
print(UserOtpResponseObject.to_json())

# convert the object into a dict
user_otp_response_object_dict = user_otp_response_object_instance.to_dict()
# create an instance of UserOtpResponseObject from a dict
user_otp_response_object_from_dict = UserOtpResponseObject.from_dict(user_otp_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


