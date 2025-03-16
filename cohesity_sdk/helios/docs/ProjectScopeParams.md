# ProjectScopeParams

Specifies the parameters for project type scope.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name of the project. | 
**project_name** | **str** | Specifies the project name. | 

## Example

```python
from cohesity_sdk.helios.models.project_scope_params import ProjectScopeParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectScopeParams from a JSON string
project_scope_params_instance = ProjectScopeParams.from_json(json)
# print the JSON string representation of the object
print(ProjectScopeParams.to_json())

# convert the object into a dict
project_scope_params_dict = project_scope_params_instance.to_dict()
# create an instance of ProjectScopeParams from a dict
project_scope_params_from_dict = ProjectScopeParams.from_dict(project_scope_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


