# LocalUserResponseParams

Specifies properties for LOCAL cohesity user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Specifies the email address of the User. | [optional] 

## Example

```python
from cohesity_sdk.models.local_user_response_params import LocalUserResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of LocalUserResponseParams from a JSON string
local_user_response_params_instance = LocalUserResponseParams.from_json(json)
# print the JSON string representation of the object
print(LocalUserResponseParams.to_json())

# convert the object into a dict
local_user_response_params_dict = local_user_response_params_instance.to_dict()
# create an instance of LocalUserResponseParams from a dict
local_user_response_params_from_dict = LocalUserResponseParams.from_dict(local_user_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


