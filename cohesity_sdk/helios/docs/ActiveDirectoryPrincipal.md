# ActiveDirectoryPrincipal

Specifies an active directory principal fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name to which the principal belongs to | [optional] 
**full_name** | **str** | Specifies the full name of the principal. | [optional] 
**name** | **str** | Specifies the name of the principal which is being added. | [optional] 
**object_class** | **str** | Specifies the type of principal, a user or a group | [optional] 
**sid** | **str** | Specifies the unique SID of the principal. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.active_directory_principal import ActiveDirectoryPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryPrincipal from a JSON string
active_directory_principal_instance = ActiveDirectoryPrincipal.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryPrincipal.to_json())

# convert the object into a dict
active_directory_principal_dict = active_directory_principal_instance.to_dict()
# create an instance of ActiveDirectoryPrincipal from a dict
active_directory_principal_from_dict = ActiveDirectoryPrincipal.from_dict(active_directory_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


