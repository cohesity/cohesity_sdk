# McmSource

Specifies a Protection Source on Helios MCM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the Protection Source. | [optional] 
**id** | **str** | Specifies the unique identifier of the Source. | [optional] 
**name** | **str** | Specifies the name of the Protection Source. | [optional] 
**source_info_list** | [**List[McmSourceInfo]**](McmSourceInfo.md) | Specifies the Source information list across all platforms. | [optional] 
**type** | **str** | Specifies the object type of the Protection Source. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_source import McmSource

# TODO update the JSON string below
json = "{}"
# create an instance of McmSource from a JSON string
mcm_source_instance = McmSource.from_json(json)
# print the JSON string representation of the object
print(McmSource.to_json())

# convert the object into a dict
mcm_source_dict = mcm_source_instance.to_dict()
# create an instance of McmSource from a dict
mcm_source_from_dict = McmSource.from_dict(mcm_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


