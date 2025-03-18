# ExistingGroupParam

Specifies the parameters for using existing protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the protection group id. | 

## Example

```python
from cohesity_sdk.cluster.models.existing_group_param import ExistingGroupParam

# TODO update the JSON string below
json = "{}"
# create an instance of ExistingGroupParam from a JSON string
existing_group_param_instance = ExistingGroupParam.from_json(json)
# print the JSON string representation of the object
print(ExistingGroupParam.to_json())

# convert the object into a dict
existing_group_param_dict = existing_group_param_instance.to_dict()
# create an instance of ExistingGroupParam from a dict
existing_group_param_from_dict = ExistingGroupParam.from_dict(existing_group_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


