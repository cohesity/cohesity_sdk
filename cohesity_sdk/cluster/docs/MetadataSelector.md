# MetadataSelector

Selector for the metadata to be exported.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_selector** | [**EntitySelector**](EntitySelector.md) |  | [optional] 
**include_environments** | **[str]** | Contains the environments info that will be exported. If this is empty, all the environments info will be exported.. | [optional] 
**include_job_descriptions** | **bool** | If true, exports the job descriptions. This is automatically true if the include_restore_tasks is true. | [optional] 
**include_policies** | **bool** | If true, exports the accessible policies. | [optional] 
**include_restore_tasks** | **bool** | If true, exports the qualified restore tasks. | [optional] 
**run_selector** | [**ProtectionRunSelector**](ProtectionRunSelector.md) |  | [optional] 
**tenant_id** | **str** | Denotes the tenant whose metadata needs to be exported | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


