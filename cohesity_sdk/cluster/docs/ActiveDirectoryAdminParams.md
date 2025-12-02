# ActiveDirectoryAdminParams

Specifies the params of a user with administrative privilege of an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password of the user. | 
**username** | **str** | Specifies the user name. | 

## Example

```python
from cohesity_sdk.cluster.models.active_directory_admin_params import ActiveDirectoryAdminParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryAdminParams from a JSON string
active_directory_admin_params_instance = ActiveDirectoryAdminParams.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryAdminParams.to_json())

# convert the object into a dict
active_directory_admin_params_dict = active_directory_admin_params_instance.to_dict()
# create an instance of ActiveDirectoryAdminParams from a dict
active_directory_admin_params_from_dict = ActiveDirectoryAdminParams.from_dict(active_directory_admin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


