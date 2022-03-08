# HeliosTenantClusterResources

A list of Sources and Storage Domains assigned to the Tenant, grouped by Cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str, none_type** | Specifies the list of cluster identifiers. The format is clusterId:clusterIncarnationId. | [optional] 
**storage_domain_names** | **[str], none_type** | List of assigned Storage Domains. | [optional] 
**source_names** | **[str], none_type** | List of completely assigned Sources. | [optional] 
**source_stats** | [**[HeliosSourceObjectsStats], none_type**](HeliosSourceObjectsStats.md) | Number of assigned objects grouped by source names. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


