# CreateViewFailoverRequest

Specifies the request parameters to create a view failover task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str, none_type** | Specifies the failover type.&lt;br&gt; &#39;Planned&#39; indicates this is a planned failover.&lt;br&gt; &#39;Unplanned&#39; indicates this is an unplanned failover, which is used when source cluster is down. | 
**planned_failover_params** | [**PlannedFailoverParams**](PlannedFailoverParams.md) |  | [optional] 
**unplanned_failover_params** | [**UnplannedFailoverParams**](UnplannedFailoverParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


