# WorkloadSubType

Specifies the Workload Sub-Type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Specifies the Id of an Entity. | [optional] 
**name** | **str** | Specifies the name of an Entity. | [optional] 
**entities** | [**List[EntityIdentifier]**](EntityIdentifier.md) | Specifies the entities part of Workload schema. | [optional] 
**var_schema** | **str** | Specifies the Schema Name of Workload. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.workload_sub_type import WorkloadSubType

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadSubType from a JSON string
workload_sub_type_instance = WorkloadSubType.from_json(json)
# print the JSON string representation of the object
print(WorkloadSubType.to_json())

# convert the object into a dict
workload_sub_type_dict = workload_sub_type_instance.to_dict()
# create an instance of WorkloadSubType from a dict
workload_sub_type_from_dict = WorkloadSubType.from_dict(workload_sub_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


