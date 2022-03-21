# ExternalTarget

External Target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the External Target. | 
**purpose_type** | **str, none_type** | Specifies the purpose of the External Target. | 
**id** | **int, none_type** | Specifies the ID of the External Target. | [optional] [readonly] 
**global_id** | **str, none_type** | Specifies the global identifier of the External Target. | [optional] 
**compression** | **str, none_type** | Specifies whether the type of compression of the External Target | [optional] 
**status** | **str, none_type** | Specifies the registration status of the External Target | [optional] [readonly] 
**error_message** | **str, none_type** | Specifies the error message if the event is in failed state. | [optional] [readonly] 
**tenant_ids** | **[str]** | Specifies the list of tenantIds for the External Target | [optional] 
**cloud_domains** | [**[CloudDomain], none_type**](CloudDomain.md) | Specifies the cloud domain information. | [optional] 
**storage_domain_name** | **str, none_type** | Specifies the storage domain associated with the target. | [optional] 
**is_worm_capable** | **bool, none_type** | Specifies whether this external target has been found to be capable of supporting WORM archives. | [optional] 
**ownership_context** | **str, none_type** | Specifies whether how this external target is being consumed either Local or FortKnox. | [optional] 
**archival_params** | [**ArchivalExternalTargetParams**](ArchivalExternalTargetParams.md) |  | [optional] 
**tiering_params** | [**TieringExternalTargetParams**](TieringExternalTargetParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


