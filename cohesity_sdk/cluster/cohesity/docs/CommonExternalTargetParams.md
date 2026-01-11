# CommonExternalTargetParams

Specifies the parameters which are common between all External Target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the External Target. | 
**purpose_type** | **str, none_type** | Specifies the purpose of the External Target. | 
**cloud_domains** | [**[CloudDomain], none_type**](CloudDomain.md) | Specifies the cloud domain information. | [optional] 
**compression** | **str, none_type** | Specifies whether the type of compression of the External Target | [optional] 
**enable_object_lock** | **bool, none_type** | Whether to enable object lock for this vault. If this field is set, all the objects written to the vault will be object locked until all the archives referring to them expire. | [optional] 
**error_message** | **str, none_type** | Specifies the error message if the event is in failed state. | [optional] [readonly] 
**global_id** | **str, none_type** | Specifies the global identifier of the External Target. | [optional] 
**id** | **int, none_type** | Specifies the ID of the External Target. | [optional] [readonly] 
**is_worm_capable** | **bool, none_type** | Specifies whether this external target has been found to be capable of supporting WORM archives. | [optional] 
**ownership_context** | **str, none_type** | Specifies whether how this external target is being consumed either Local or FortKnox. | [optional] 
**status** | **str, none_type** | Specifies the registration status of the External Target | [optional] [readonly] 
**storage_domain_name** | **str, none_type** | Specifies the storage domain associated with the target. | [optional] 
**tenant_ids** | **[str]** | Specifies the list of tenantIds for the External Target | [optional] 
**use_for_apollo_mr_store** | **bool, none_type** | Specifies whether this external target is used to store apollo mr records. | [optional] 
**use_rolling_object_lock** | **bool, none_type** | Whether the vault should use rolling object lock. | [optional] 
**worm_lock_in_compliance_mode** | **bool, none_type** | Whether archives to this vault should use compliance mode when adding data locks to objects. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


