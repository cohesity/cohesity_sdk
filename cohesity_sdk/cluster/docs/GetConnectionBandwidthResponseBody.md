# GetConnectionBandwidthResponseBody

The response body for put and get connection bandwidth.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str, none_type** | The tenant Id corresponding to this request. | 
**connection_id** | **int, none_type** | Connection Id for which bandwidth settings are to be returned | [optional] 
**connector_groups** | [**[ConnectorGroup], none_type**](ConnectorGroup.md) | Specifies the list of connector groups. | [optional] 
**connector_group_id** | **int, none_type** | Specifies the connector group id of connector groups. | [optional] 
**download** | [**[BandwidthLimit], none_type**](BandwidthLimit.md) | Specifies the max rate limit at which we download the data. | [optional] 
**timezone** | **str, none_type** | Specifies a time zone for the specified time period. The time zone is defined in the following format: &#39;Area/Location&#39;, for example: &#39;America/New_York&#39;. | [optional] 
**upload** | [**[BandwidthLimit], none_type**](BandwidthLimit.md) | Specifies the max rate limit at which we upload the data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


