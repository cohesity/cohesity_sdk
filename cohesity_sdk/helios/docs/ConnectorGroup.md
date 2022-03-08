# ConnectorGroup

Specify a group of connectors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the id of the group. | [optional] 
**name** | **str, none_type** | Specifies the name of the group. | [optional] 
**connectors** | **[int]** | Specifies the ids of the connectors in the group. | [optional] 
**download_bandwidth_limts** | [**[BandwidthLimit], none_type**](BandwidthLimit.md) | Specifies the max rate limit at which we download the data. | [optional] 
**upload_bandwidth_limts** | [**[BandwidthLimit], none_type**](BandwidthLimit.md) | Specifies the max rate limit at which we upload the data. | [optional] 
**timezone** | **str, none_type** | Specifies a time zone for the specified time period. The time zone is defined in the following format: &#39;Area/Location&#39;, for example: &#39;America/New_York&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


