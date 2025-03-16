# HeliosCommonSearchIndexedObjectsResponseParams

Specifies the common search indexed objects response params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_errors** | [**List[HeliosSearchIndexedObjectsClusterError]**](HeliosSearchIndexedObjectsClusterError.md) | A List of errors that occured on a subset of clusters. | [optional] 
**count** | **int** | Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 
**object_type** | **str** | Specifies the object type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_common_search_indexed_objects_response_params import HeliosCommonSearchIndexedObjectsResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosCommonSearchIndexedObjectsResponseParams from a JSON string
helios_common_search_indexed_objects_response_params_instance = HeliosCommonSearchIndexedObjectsResponseParams.from_json(json)
# print the JSON string representation of the object
print(HeliosCommonSearchIndexedObjectsResponseParams.to_json())

# convert the object into a dict
helios_common_search_indexed_objects_response_params_dict = helios_common_search_indexed_objects_response_params_instance.to_dict()
# create an instance of HeliosCommonSearchIndexedObjectsResponseParams from a dict
helios_common_search_indexed_objects_response_params_from_dict = HeliosCommonSearchIndexedObjectsResponseParams.from_dict(helios_common_search_indexed_objects_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


