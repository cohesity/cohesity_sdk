# HeliosSourceObjectsStats

Number of assigned objects to a tenant for given source name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_assigned_objects** | **int** | Number of objects assigned. | [optional] 
**source_name** | **str** | Name of the source | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_source_objects_stats import HeliosSourceObjectsStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosSourceObjectsStats from a JSON string
helios_source_objects_stats_instance = HeliosSourceObjectsStats.from_json(json)
# print the JSON string representation of the object
print(HeliosSourceObjectsStats.to_json())

# convert the object into a dict
helios_source_objects_stats_dict = helios_source_objects_stats_instance.to_dict()
# create an instance of HeliosSourceObjectsStats from a dict
helios_source_objects_stats_from_dict = HeliosSourceObjectsStats.from_dict(helios_source_objects_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


