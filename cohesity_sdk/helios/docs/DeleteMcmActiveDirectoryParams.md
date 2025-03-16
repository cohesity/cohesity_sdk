# DeleteMcmActiveDirectoryParams

Specifies the request to delete an Active Directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_params** | [**AdminParams**](AdminParams.md) | Specifies the params of a user with administrative privilege of this Active Directory. | 

## Example

```python
from cohesity_sdk.helios.models.delete_mcm_active_directory_params import DeleteMcmActiveDirectoryParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMcmActiveDirectoryParams from a JSON string
delete_mcm_active_directory_params_instance = DeleteMcmActiveDirectoryParams.from_json(json)
# print the JSON string representation of the object
print(DeleteMcmActiveDirectoryParams.to_json())

# convert the object into a dict
delete_mcm_active_directory_params_dict = delete_mcm_active_directory_params_instance.to_dict()
# create an instance of DeleteMcmActiveDirectoryParams from a dict
delete_mcm_active_directory_params_from_dict = DeleteMcmActiveDirectoryParams.from_dict(delete_mcm_active_directory_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


