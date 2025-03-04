# NewGroupParam

Specifies the parameters for using a new protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the new protection group. | 
**policy_id** | **str** | Specifies the policy id of the new protection group. | 
**storage_domain_id** | **int** | Specifies the storage domain id of the new protection group. | 

## Example

```python
from cohesity_sdk.models.new_group_param import NewGroupParam

# TODO update the JSON string below
json = "{}"
# create an instance of NewGroupParam from a JSON string
new_group_param_instance = NewGroupParam.from_json(json)
# print the JSON string representation of the object
print(NewGroupParam.to_json())

# convert the object into a dict
new_group_param_dict = new_group_param_instance.to_dict()
# create an instance of NewGroupParam from a dict
new_group_param_from_dict = NewGroupParam.from_dict(new_group_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


