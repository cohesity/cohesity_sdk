# AgentInformation

Specifies the agent details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str, none_type** | Specifies the status of agent connection. | [optional] 
**support_status** | **str, none_type** | Specifies the whether agent version is compatible with cluster version ro use various features. | [optional] 
**agent_sw_version** | **str, none_type** | Specifies the software version of the agent | [optional] 
**last_fetched_time_in_usecs** | **int, none_type** | Specifies the time in usecs when the last agent info was fetched. | [optional] 
**host_setting_checks** | [**[HostSettingCheck], none_type**](HostSettingCheck.md) | Specifies the list of host checks and its results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


