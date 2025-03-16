# ActiveDirectoryPrincipalParams

Specifies the params of Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name of the Active Directory. | [optional] 
**parent_domain** | **str** | Specifies the parent domain name which is registered. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.active_directory_principal_params import ActiveDirectoryPrincipalParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryPrincipalParams from a JSON string
active_directory_principal_params_instance = ActiveDirectoryPrincipalParams.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryPrincipalParams.to_json())

# convert the object into a dict
active_directory_principal_params_dict = active_directory_principal_params_instance.to_dict()
# create an instance of ActiveDirectoryPrincipalParams from a dict
active_directory_principal_params_from_dict = ActiveDirectoryPrincipalParams.from_dict(active_directory_principal_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


