# CommonExternalTargetParams

Specifies the parameters which are common between all External Target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the External Target. | 
**purpose_type** | **str, none_type** | Specifies the purpose of the External Target. | 
**cloud_domains** | [**[CloudDomain], none_type**](CloudDomain.md) | Specifies the cloud domain information. | [optional] 
**compression** | **str, none_type** | Specifies whether the type of compression of the External Target | [optional] 
**error_message** | **str, none_type** | Specifies the error message if the event is in failed state. | [optional] [readonly] 
**global_id** | **str, none_type** | Specifies the global identifier of the External Target. | [optional] 
**id** | **int, none_type** | Specifies the ID of the External Target. | [optional] [readonly] 
**is_worm_capable** | **bool, none_type** | Specifies whether this external target has been found to be capable of supporting WORM archives. | [optional] 
**ownership_context** | **str, none_type** | Specifies whether how this external target is being consumed either Local or FortKnox. | [optional] 
**status** | **str, none_type** | Specifies the registration status of the External Target | [optional] [readonly] 
**storage_domain_name** | **str, none_type** | Specifies the storage domain associated with the target. | [optional] 
**tenant_ids** | **[str]** | Specifies the list of tenantIds for the External Target | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


