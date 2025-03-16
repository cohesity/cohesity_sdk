# PrincipalParams

Specifies a principal fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_params** | [**ActiveDirectoryPrincipalParams**](ActiveDirectoryPrincipalParams.md) | Specifies active directory details of its active directory if the principal if from active directory. | [optional] 
**clusters** | **List[str]** | Specifies a list of clusters associated with this Principal. They should be in a string with the format &#39;{cluster ID}:{cluster incarnation ID}&#39;. | [optional] 
**created_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this Principal was created. | [optional] 
**description** | **str** | Specifies the desciption of the principal. | [optional] 
**effective_time_usecs** | **int** | Specifies the starting timestamp in microseconds since the epoch when this principal will be able to log in. | [optional] 
**last_updated_time_usecs** | **int** | Specifies the timestamp in microseconds since the epoch when this Principal was updated. | [optional] 
**name** | **str** | Specifies the name of the principal which is being added. | 
**object_class** | **str** | Specifies the type of principal, a user or a group | 
**principal_type** | **str** | Specifies the type of principal, a local, an sso or an active directory. | [optional] 
**roles** | **List[str]** | Specifies the role assigned to the principal. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.principal_params import PrincipalParams

# TODO update the JSON string below
json = "{}"
# create an instance of PrincipalParams from a JSON string
principal_params_instance = PrincipalParams.from_json(json)
# print the JSON string representation of the object
print(PrincipalParams.to_json())

# convert the object into a dict
principal_params_dict = principal_params_instance.to_dict()
# create an instance of PrincipalParams from a dict
principal_params_from_dict = PrincipalParams.from_dict(principal_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


