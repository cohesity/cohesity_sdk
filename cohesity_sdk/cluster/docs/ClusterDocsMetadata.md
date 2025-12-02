# ClusterDocsMetadata

Specifies the docs related metadata specific to the cluster. This metadata mainly consists of any external hyperlinks to service provider's documentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | **str** | Specifies the purpose for having external hyperlink to documentation. | [optional] 
**url** | **str** | Specifies the URL to access the endpoint for the given documentation purpose. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_docs_metadata import ClusterDocsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDocsMetadata from a JSON string
cluster_docs_metadata_instance = ClusterDocsMetadata.from_json(json)
# print the JSON string representation of the object
print(ClusterDocsMetadata.to_json())

# convert the object into a dict
cluster_docs_metadata_dict = cluster_docs_metadata_instance.to_dict()
# create an instance of ClusterDocsMetadata from a dict
cluster_docs_metadata_from_dict = ClusterDocsMetadata.from_dict(cluster_docs_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


