# ClusterSLAMetadata

Specifies the SLA related metadata associated with the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_sla** | **int, none_type** | Specifies the default SLA in minutes at cluster level which will be applied as default across all protection groups. This value is only used by UI to populate the default value. | [optional] 
**minimum_sla** | **int, none_type** | Specifies the minimum SLA in minutes at cluster level which will be validated against all protection groups SLA configuration. If the provided SLA at protection group creation or update is less than this value then protection group request will be invalidated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


