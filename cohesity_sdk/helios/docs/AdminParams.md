# AdminParams

Specifies the params of a user with administrative privilege of an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password of the user. | 
**username** | **str** | Specifies the user name. | 

## Example

```python
from cohesity_sdk.helios.models.admin_params import AdminParams

# TODO update the JSON string below
json = "{}"
# create an instance of AdminParams from a JSON string
admin_params_instance = AdminParams.from_json(json)
# print the JSON string representation of the object
print(AdminParams.to_json())

# convert the object into a dict
admin_params_dict = admin_params_instance.to_dict()
# create an instance of AdminParams from a dict
admin_params_from_dict = AdminParams.from_dict(admin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


