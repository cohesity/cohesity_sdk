# ReplicatedViewNameConfig

Specifies an object protected by a View Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_view_id** | **int** | Specifies the ID of the protected view. | 
**use_same_view_name** | **bool** | Specifies if the remote view name to be kept is same as the source view name. If this field is true, viewName field will be ignored. | [optional] 
**view_name** | **str** | Specifies the name of the remote view. This field is only used when useSameViewName is false. If useSameViewName is true, this field is not used. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.replicated_view_name_config import ReplicatedViewNameConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicatedViewNameConfig from a JSON string
replicated_view_name_config_instance = ReplicatedViewNameConfig.from_json(json)
# print the JSON string representation of the object
print(ReplicatedViewNameConfig.to_json())

# convert the object into a dict
replicated_view_name_config_dict = replicated_view_name_config_instance.to_dict()
# create an instance of ReplicatedViewNameConfig from a dict
replicated_view_name_config_from_dict = ReplicatedViewNameConfig.from_dict(replicated_view_name_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


