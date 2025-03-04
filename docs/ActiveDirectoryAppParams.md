# ActiveDirectoryAppParams

Specifies the Active Directory special parameters for the Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** | Specifies the application id of the Active Directory instance. | [optional] 
**app_name** | **str** | Specifies the application name of the Active Directory instance. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.active_directory_app_params import ActiveDirectoryAppParams

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveDirectoryAppParams from a JSON string
active_directory_app_params_instance = ActiveDirectoryAppParams.from_json(json)
# print the JSON string representation of the object
print(ActiveDirectoryAppParams.to_json())

# convert the object into a dict
active_directory_app_params_dict = active_directory_app_params_instance.to_dict()
# create an instance of ActiveDirectoryAppParams from a dict
active_directory_app_params_from_dict = ActiveDirectoryAppParams.from_dict(active_directory_app_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


