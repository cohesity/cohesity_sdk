# BandwidthThrottling

Specifies settings for limiting the data transfer rate between the local and remote Clusters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_limit_bytes_per_sec** | **int, none_type** | Specifies the maximum allowed data transfer rate between the local Cluster and remote Clusters. | [optional] 
**timezone** | **str, none_type** | Specifies a time zone for the specified time period. | [optional] 
**bandwidth_limit_overrides** | [**[BandwidthThrottlingOverride]**](BandwidthThrottlingOverride.md) | Specifies the max rate limit at which we upload the data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


