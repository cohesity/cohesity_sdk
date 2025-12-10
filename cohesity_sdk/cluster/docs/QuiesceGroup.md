# QuiesceGroup

Specifies the quiesce group for kubernetes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quiesce_mode** | **str** | Specifies quiesce mode for applying quiesce rules. | 
**quiesce_rules** | [**List[QuiesceRule]**](QuiesceRule.md) | Specifies a list of quiesce rules. | 

## Example

```python
from cohesity_sdk.cluster.models.quiesce_group import QuiesceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of QuiesceGroup from a JSON string
quiesce_group_instance = QuiesceGroup.from_json(json)
# print the JSON string representation of the object
print(QuiesceGroup.to_json())

# convert the object into a dict
quiesce_group_dict = quiesce_group_instance.to_dict()
# create an instance of QuiesceGroup from a dict
quiesce_group_from_dict = QuiesceGroup.from_dict(quiesce_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


