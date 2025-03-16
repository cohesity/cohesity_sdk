# ActiveDirectoryPrincipalList

Specifies active directory principals search results, the paginationtoken will be used in future, currently, this will return all the principal in the result as it is, without pagination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_token** | **str** | Specifies page number of AD principals in the search results. | [optional] 
**principals** | [**List[ActiveDirectoryPrincipal]**](ActiveDirectoryPrincipal.md) | Specifies AD principals in the search results. | [optional] 
**total** | **int** | Specifies total number of AD principals in the search results. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.active_directory_principal_list import ActiveDirectoryPrincipalList

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryPrincipalList from a JSON string
active_directory_principal_list_instance = ActiveDirectoryPrincipalList.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryPrincipalList.to_json())

# convert the object into a dict
active_directory_principal_list_dict = active_directory_principal_list_instance.to_dict()
# create an instance of ActiveDirectoryPrincipalList from a dict
active_directory_principal_list_from_dict = ActiveDirectoryPrincipalList.from_dict(active_directory_principal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


