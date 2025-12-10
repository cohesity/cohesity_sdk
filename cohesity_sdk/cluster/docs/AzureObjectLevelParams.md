# AzureObjectLevelParams

Specifies the Azure object level settings for object protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_exclusion_params** | [**AzureDiskExclusionParams**](AzureDiskExclusionParams.md) |  | [optional] 
**exclude_object_ids** | **List[Optional[int]]** | Specifies the list of IDs of the objects not to be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag. This can be used to ignore specific objects (can include tags) under a parent object which has been included for protection. | [optional] 
**id** | **int** | Specifies the id of the object being protected. This can be a leaf level or non leaf level object. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_object_level_params import AzureObjectLevelParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureObjectLevelParams from a JSON string
azure_object_level_params_instance = AzureObjectLevelParams.from_json(json)
# print the JSON string representation of the object
print(AzureObjectLevelParams.to_json())

# convert the object into a dict
azure_object_level_params_dict = azure_object_level_params_instance.to_dict()
# create an instance of AzureObjectLevelParams from a dict
azure_object_level_params_from_dict = AzureObjectLevelParams.from_dict(azure_object_level_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


