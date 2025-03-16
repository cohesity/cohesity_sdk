# WorkloadStatsSchema

Specifies the workload types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Specifies the Id of an Entity. | [optional] 
**name** | **str** | Specifies the name of an Entity. | [optional] 
**entities** | [**List[EntityIdentifier]**](EntityIdentifier.md) | Specifies the entities part of Workload schema. | [optional] 
**var_schema** | **str** | Specifies the Schema Name of Workload. | [optional] 
**sub_types** | [**List[WorkloadSubType]**](WorkloadSubType.md) | Specifies the Workload Sub-Types. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.workload_stats_schema import WorkloadStatsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkloadStatsSchema from a JSON string
workload_stats_schema_instance = WorkloadStatsSchema.from_json(json)
# print the JSON string representation of the object
print(WorkloadStatsSchema.to_json())

# convert the object into a dict
workload_stats_schema_dict = workload_stats_schema_instance.to_dict()
# create an instance of WorkloadStatsSchema from a dict
workload_stats_schema_from_dict = WorkloadStatsSchema.from_dict(workload_stats_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


