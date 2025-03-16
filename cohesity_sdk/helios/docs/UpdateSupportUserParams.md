# UpdateSupportUserParams

Specifies the support user params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Specifies the current password of the user. This is required when trying to update the current user&#39;s password. | [optional] 
**enable_sudo_access** | **bool** | If set to true, sudo access will be enabled for the user. If null, the endpoint will not attempt to alter sudo access privilege for the support user. | [optional] 
**new_password** | **str** | Specifies the new password for the support user. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_support_user_params import UpdateSupportUserParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSupportUserParams from a JSON string
update_support_user_params_instance = UpdateSupportUserParams.from_json(json)
# print the JSON string representation of the object
print(UpdateSupportUserParams.to_json())

# convert the object into a dict
update_support_user_params_dict = update_support_user_params_instance.to_dict()
# create an instance of UpdateSupportUserParams from a dict
update_support_user_params_from_dict = UpdateSupportUserParams.from_dict(update_support_user_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


