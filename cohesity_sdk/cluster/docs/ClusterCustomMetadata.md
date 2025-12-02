# ClusterCustomMetadata

Specifies the list of custom properties associated with the cluster. API callers can choose to set the following properties using provided key and value fields. The input values must always be in the string format and each key must be unique. The callers should ensure that no sensitive information such as passwords is sent in the custom metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Specifies the key for the customer cluster metadata. | [optional] 
**value** | **str** | Specifies the value for the above key. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_custom_metadata import ClusterCustomMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCustomMetadata from a JSON string
cluster_custom_metadata_instance = ClusterCustomMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterCustomMetadata.to_json())

# convert the object into a dict
cluster_custom_metadata_dict = cluster_custom_metadata_instance.to_dict()
# create an instance of ClusterCustomMetadata from a dict
cluster_custom_metadata_from_dict = ClusterCustomMetadata.from_dict(cluster_custom_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


