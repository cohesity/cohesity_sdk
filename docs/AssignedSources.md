# AssignedSources

Sources assigned to a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_ids** | **List[int]** | Specifies a list of source Ids assigned to a principal. | [optional] 
**view_ids** | **List[int]** | Specifies a list of view Ids assigned to a principal. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.assigned_sources import AssignedSources

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedSources from a JSON string
assigned_sources_instance = AssignedSources.from_json(json)
# print the JSON string representation of the object
print(AssignedSources.to_json())

# convert the object into a dict
assigned_sources_dict = assigned_sources_instance.to_dict()
# create an instance of AssignedSources from a dict
assigned_sources_from_dict = AssignedSources.from_dict(assigned_sources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


