# RecoverTarget

Specifies the target entity to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**parent_source_id** | **int** | Specifies the id of the parent source of the target. | [optional] [readonly] 
**parent_source_name** | **str** | Specifies the name of the parent source of the target. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.recover_target import RecoverTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverTarget from a JSON string
recover_target_instance = RecoverTarget.from_json(json)
# print the JSON string representation of the object
print(RecoverTarget.to_json())

# convert the object into a dict
recover_target_dict = recover_target_instance.to_dict()
# create an instance of RecoverTarget from a dict
recover_target_from_dict = RecoverTarget.from_dict(recover_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


