# UpdateRoleParameters

Specifies the parameters to update a Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description message for the Role. | [optional] 
**privileges** | **List[str]** | Specifies the list of Privileges of the Role. | 

## Example

```python
from cohesity_sdk.helios.models.update_role_parameters import UpdateRoleParameters

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleParameters from a JSON string
update_role_parameters_instance = UpdateRoleParameters.from_json(json)
# print the JSON string representation of the object
print(UpdateRoleParameters.to_json())

# convert the object into a dict
update_role_parameters_dict = update_role_parameters_instance.to_dict()
# create an instance of UpdateRoleParameters from a dict
update_role_parameters_from_dict = UpdateRoleParameters.from_dict(update_role_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


