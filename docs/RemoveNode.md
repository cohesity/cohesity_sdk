# RemoveNode

Specifies details of node removal response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies id of the node. | [optional] 
**marked_for_removal** | **bool** | If true, Node is marked for removal. | [optional] 
**timestamp_secs** | **int** | Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds). | [optional] 
**validation_checks** | [**List[PreCheckValidation]**](PreCheckValidation.md) | Specifies the pre-check validations results. | [optional] 

## Example

```python
from cohesity_sdk.models.remove_node import RemoveNode

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveNode from a JSON string
remove_node_instance = RemoveNode.from_json(json)
# print the JSON string representation of the object
print(RemoveNode.to_json())

# convert the object into a dict
remove_node_dict = remove_node_instance.to_dict()
# create an instance of RemoveNode from a dict
remove_node_from_dict = RemoveNode.from_dict(remove_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


