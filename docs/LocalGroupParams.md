# LocalGroupParams

Specifies properties for LOCAL Cohesity group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_sids** | **List[str]** | Specifies the LOCAL users which are part of this group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.local_group_params import LocalGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of LocalGroupParams from a JSON string
local_group_params_instance = LocalGroupParams.from_json(json)
# print the JSON string representation of the object
print(LocalGroupParams.to_json())

# convert the object into a dict
local_group_params_dict = local_group_params_instance.to_dict()
# create an instance of LocalGroupParams from a dict
local_group_params_from_dict = LocalGroupParams.from_dict(local_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


