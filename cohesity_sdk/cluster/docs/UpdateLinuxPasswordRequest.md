# UpdateLinuxPasswordRequest

Specifies the linux user params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** | Specifies the current password of the user. This is required when trying to update the current user&#39;s password. | [optional] 
**new_password** | **str** | Specifies the new linux password. | [optional] 
**username** | **str** | Specifies the linux username for which the password will be updated. | 
**verify_password** | **bool** | True if request is only to verify if current password matches with set password. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_linux_password_request import UpdateLinuxPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLinuxPasswordRequest from a JSON string
update_linux_password_request_instance = UpdateLinuxPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateLinuxPasswordRequest.to_json())

# convert the object into a dict
update_linux_password_request_dict = update_linux_password_request_instance.to_dict()
# create an instance of UpdateLinuxPasswordRequest from a dict
update_linux_password_request_from_dict = UpdateLinuxPasswordRequest.from_dict(update_linux_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


