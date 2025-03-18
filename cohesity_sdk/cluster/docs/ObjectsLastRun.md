# ObjectsLastRun

Last protection run info of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_last_runs** | [**List[ObjectLastRun]**](ObjectLastRun.md) | Specifies a list of last protection runs of objects. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.objects_last_run import ObjectsLastRun

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsLastRun from a JSON string
objects_last_run_instance = ObjectsLastRun.from_json(json)
# print the JSON string representation of the object
print(ObjectsLastRun.to_json())

# convert the object into a dict
objects_last_run_dict = objects_last_run_instance.to_dict()
# create an instance of ObjectsLastRun from a dict
objects_last_run_from_dict = ObjectsLastRun.from_dict(objects_last_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


