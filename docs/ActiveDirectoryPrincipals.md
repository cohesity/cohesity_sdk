# ActiveDirectoryPrincipals

Response of Active directory principals.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principals** | [**List[ActiveDirectoryPrincipal]**](ActiveDirectoryPrincipal.md) | A list of Active directory principals | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.active_directory_principals import ActiveDirectoryPrincipals

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryPrincipals from a JSON string
active_directory_principals_instance = ActiveDirectoryPrincipals.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryPrincipals.to_json())

# convert the object into a dict
active_directory_principals_dict = active_directory_principals_instance.to_dict()
# create an instance of ActiveDirectoryPrincipals from a dict
active_directory_principals_from_dict = ActiveDirectoryPrincipals.from_dict(active_directory_principals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


