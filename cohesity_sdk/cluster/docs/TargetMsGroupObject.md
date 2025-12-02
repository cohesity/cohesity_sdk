# TargetMsGroupObject

Specifies the existing target group to restore to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**primary_smtp_address** | **str** | Specifies the primary SMTP Address of the target group. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.target_ms_group_object import TargetMsGroupObject

# TODO update the JSON string below
json = "{}"
# create an instance of TargetMsGroupObject from a JSON string
target_ms_group_object_instance = TargetMsGroupObject.from_json(json)
# print the JSON string representation of the object
print(TargetMsGroupObject.to_json())

# convert the object into a dict
target_ms_group_object_dict = target_ms_group_object_instance.to_dict()
# create an instance of TargetMsGroupObject from a dict
target_ms_group_object_from_dict = TargetMsGroupObject.from_dict(target_ms_group_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


