# IbmTenantMeteringConfig

Specifies the metering configuration that will be used for cohesity cluster to send the billing details to IBM billing service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**part_ids** | **[str]** | Specifies the list of part identifiers used for metrics identification. | [optional] 
**submission_interval_in_secs** | **int, none_type** | Specifies the frequency in seconds at which the metrics will be pushed to IBM billing service from cluster. | [optional] 
**url** | **str, none_type** | Specifies the base metering URL that will be used by cluster to send the billing information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


