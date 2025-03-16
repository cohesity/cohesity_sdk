# HeliosCommonSearchIndexedObjectsRequestParams

Specifies the common params to search for global indexed objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifiers** | **List[str]** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | [optional] 
**count** | **int** | Specifies the number of indexed objects to be fetched. | [optional] 
**object_type** | **str** | Specifies the object type to be searched for. | 
**region_ids** | **List[str]** | List of Regions to filter from. | [optional] 
**source_uuids** | **List[str]** | Specifies a list of source UUIDs. Only matches found in these sources will be returned. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_common_search_indexed_objects_request_params import HeliosCommonSearchIndexedObjectsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosCommonSearchIndexedObjectsRequestParams from a JSON string
helios_common_search_indexed_objects_request_params_instance = HeliosCommonSearchIndexedObjectsRequestParams.from_json(json)
# print the JSON string representation of the object
print(HeliosCommonSearchIndexedObjectsRequestParams.to_json())

# convert the object into a dict
helios_common_search_indexed_objects_request_params_dict = helios_common_search_indexed_objects_request_params_instance.to_dict()
# create an instance of HeliosCommonSearchIndexedObjectsRequestParams from a dict
helios_common_search_indexed_objects_request_params_from_dict = HeliosCommonSearchIndexedObjectsRequestParams.from_dict(helios_common_search_indexed_objects_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


