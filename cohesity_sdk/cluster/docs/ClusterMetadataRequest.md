# ClusterMetadataRequest

Specifies the cluster metadata request details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_methods** | [**ClusterAuthMethodsMetadata**](ClusterAuthMethodsMetadata.md) |  | 
**custom_properties** | [**[ClusterCustomMetadata], none_type**](ClusterCustomMetadata.md) | Specifies the list of custom properties associated with the cluster. API caller can choose to set the following properties using provided key and value fields. The input values must always be in the string format and each key must be unique. | [optional] 
**docs** | [**[ClusterDocsMetadata], none_type**](ClusterDocsMetadata.md) | Specifies the docs related metadata specific to the cluster. This metadata mainly consists of any external hyperlinks to service provider&#39;s documentation. | [optional] 
**service_endpoints** | [**[ServiceEndpointsMetadata], none_type**](ServiceEndpointsMetadata.md) | Specifies the list of service endpoints that can be configured based on the environnment. Each service configuration must be specified only once. If same service is specified multiple times, the API will return validation error. | [optional] 
**sla** | [**ClusterSLAMetadata**](ClusterSLAMetadata.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


