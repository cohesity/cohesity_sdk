# ClusterMetadataRequest

Specifies the cluster metadata request details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_methods** | [**ClusterAuthMethodsMetadata**](ClusterAuthMethodsMetadata.md) |  | 
**custom_properties** | [**List[ClusterCustomMetadata]**](ClusterCustomMetadata.md) | Specifies the list of custom properties associated with the cluster. API caller can choose to set the following properties using provided key and value fields. The input values must always be in the string format and each key must be unique. | [optional] 
**docs** | [**List[ClusterDocsMetadata]**](ClusterDocsMetadata.md) | Specifies the docs related metadata specific to the cluster. This metadata mainly consists of any external hyperlinks to service provider&#39;s documentation. | [optional] 
**service_endpoints** | [**List[ServiceEndpointsMetadata]**](ServiceEndpointsMetadata.md) | Specifies the list of service endpoints that can be configured based on the environnment. Each service configuration must be specified only once. If same service is specified multiple times, the API will return validation error. | [optional] 
**sla** | [**ClusterSLAMetadata**](ClusterSLAMetadata.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_metadata_request import ClusterMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMetadataRequest from a JSON string
cluster_metadata_request_instance = ClusterMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterMetadataRequest.to_json())

# convert the object into a dict
cluster_metadata_request_dict = cluster_metadata_request_instance.to_dict()
# create an instance of ClusterMetadataRequest from a dict
cluster_metadata_request_from_dict = ClusterMetadataRequest.from_dict(cluster_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


