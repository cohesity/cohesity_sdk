# PrincipalList

Specifies the list of the principals in helios.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination_token** | **str** | Specifies page number of AD principals in the search results. | [optional] 
**principals** | [**List[Principal]**](Principal.md) | Specifies AD principals in the search results. | [optional] 
**total** | **int** | Specifies total number of principals in helios. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.principal_list import PrincipalList

# TODO update the JSON string below
json = "{}"
# create an instance of PrincipalList from a JSON string
principal_list_instance = PrincipalList.from_json(json)
# print the JSON string representation of the object
print(PrincipalList.to_json())

# convert the object into a dict
principal_list_dict = principal_list_instance.to_dict()
# create an instance of PrincipalList from a dict
principal_list_from_dict = PrincipalList.from_dict(principal_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


