# PlannedFailoverParams

Specifies parameters of a planned failover.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str, none_type** | Spcifies the planned failover type.&lt;br&gt; &#39;Prepare&#39; indicates this is a preparation for failover.&lt;br&gt; &#39;Finalize&#39; indicates this is finalization of failover. After this is done, the view can be used as source view. | 
**prepare_planned_failver_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters of preparation of a planned failover. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


