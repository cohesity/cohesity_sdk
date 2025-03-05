# CreateRoleParameters

Specifies the parameters to create a Role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description message for the Role. | [optional] 
**privileges** | **List[str]** | Specifies the list of Privileges of the Role. | 
**name** | **str** | Specifies the Role name. | 

## Example

```python
from cohesity_sdk.models.create_role_parameters import CreateRoleParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleParameters from a JSON string
create_role_parameters_instance = CreateRoleParameters.from_json(json)
# print the JSON string representation of the object
print(CreateRoleParameters.to_json())

# convert the object into a dict
create_role_parameters_dict = create_role_parameters_instance.to_dict()
# create an instance of CreateRoleParameters from a dict
create_role_parameters_from_dict = CreateRoleParameters.from_dict(create_role_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


