# SearchActiveDirectoryPrincipalsParams

Specifies the request to search for principals in an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_name** | **str** | Specifies the domain name. | 
**include_computers** | **bool** | Specifies whether to include the machines in the search. | [optional] 
**include_service_accounts** | **bool** | Specifies if the service accounts in AD has to be included in the search results. | [optional] 
**parent_domain** | **str** | Specifies the parent domain name which is registered. | [optional] 
**principal_type** | **str** | Specifies which type of principal to search. | [optional] 
**search_term** | **str** | Specifies the search key to search for the AD Principal. | 

## Example

```python
from cohesity_sdk.helios.models.search_active_directory_principals_params import SearchActiveDirectoryPrincipalsParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchActiveDirectoryPrincipalsParams from a JSON string
search_active_directory_principals_params_instance = SearchActiveDirectoryPrincipalsParams.from_json(json)
# print the JSON string representation of the object
print(SearchActiveDirectoryPrincipalsParams.to_json())

# convert the object into a dict
search_active_directory_principals_params_dict = search_active_directory_principals_params_instance.to_dict()
# create an instance of SearchActiveDirectoryPrincipalsParams from a dict
search_active_directory_principals_params_from_dict = SearchActiveDirectoryPrincipalsParams.from_dict(search_active_directory_principals_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


