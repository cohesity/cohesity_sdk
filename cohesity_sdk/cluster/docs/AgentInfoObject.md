# AgentInfoObject

Specifies the upgrade state of the agent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int, none_type** | Specifies the time when the upgrade for an agent completed as a Unix epoch Timestamp (in microseconds). | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**name** | **str, none_type** | Specifies the name of the source where the agent is installed. | [optional] 
**previous_software_version** | **str, none_type** | Specifies the software version of the agent before upgrade. | [optional] 
**start_time_usecs** | **int, none_type** | Specifies the time when the upgrade for an agent started as a Unix epoch Timestamp (in microseconds). | [optional] 
**status** | **str, none_type** | Specifies the upgrade status of the agent.&lt;br&gt; &#39;Scheduled&#39; indicates that upgrade for the agent is yet to start.&lt;br&gt; &#39;Started&#39; indicates that upgrade for the agent is started.&lt;br&gt; &#39;Succeeded&#39; indicates that agent was upgraded successfully.&lt;br&gt; &#39;Failed&#39; indicates that upgrade for the agent has failed.&lt;br&gt; &#39;Skipped&#39; indicates that upgrade for the agent was skipped. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


