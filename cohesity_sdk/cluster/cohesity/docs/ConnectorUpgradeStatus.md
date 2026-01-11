# ConnectorUpgradeStatus

Specifies upgrade status for the data-source connector. For example when the upgrade started, current status of the upgrade, errors for upgrade failure etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Specifies the last fetched upgrade status of the connector. | 
**last_status_fetched_timestamp_msecs** | **int, none_type** | Specifies the last timestamp in UNIX time (milliseconds) when the connector upgrade status was fetched. | [optional] 
**message** | **str, none_type** | Specifies error message for upgrade failure. | [optional] 
**start_timestamp_m_secs** | **int, none_type** | Specifies the last timestamp in UNIX time (milliseconds) when the connector upgrade was triggered. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


