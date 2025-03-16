# HeliosSearchIndexedObjectsClusterError

The error from an individual cluster while calling MCM Search Indexed Objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | clusterIdentifier for the error. | [optional] 
**error_message** | **str** | The error message. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_search_indexed_objects_cluster_error import HeliosSearchIndexedObjectsClusterError

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosSearchIndexedObjectsClusterError from a JSON string
helios_search_indexed_objects_cluster_error_instance = HeliosSearchIndexedObjectsClusterError.from_json(json)
# print the JSON string representation of the object
print(HeliosSearchIndexedObjectsClusterError.to_json())

# convert the object into a dict
helios_search_indexed_objects_cluster_error_dict = helios_search_indexed_objects_cluster_error_instance.to_dict()
# create an instance of HeliosSearchIndexedObjectsClusterError from a dict
helios_search_indexed_objects_cluster_error_from_dict = HeliosSearchIndexedObjectsClusterError.from_dict(helios_search_indexed_objects_cluster_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


