# BasicTaskInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Basic Task. | [optional] 
**task_id** | **str** | Id of the Basic task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.basic_task_info import BasicTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BasicTaskInfo from a JSON string
basic_task_info_instance = BasicTaskInfo.from_json(json)
# print the JSON string representation of the object
print(BasicTaskInfo.to_json())

# convert the object into a dict
basic_task_info_dict = basic_task_info_instance.to_dict()
# create an instance of BasicTaskInfo from a dict
basic_task_info_from_dict = BasicTaskInfo.from_dict(basic_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


