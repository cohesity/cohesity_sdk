# CreateViewFailoverRequest

Specifies the request parameters to create a view failover task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str, none_type** | Specifies the failover type.&lt;br&gt; &#39;Planned&#39; indicates this is a planned failover.&lt;br&gt; &#39;Unplanned&#39; indicates this is an unplanned failover, which is used when source cluster is down. | 
**planned_failover_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters to create a planned failover. | [optional] 
**unplanned_failover_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters to create an unplanned failover. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


