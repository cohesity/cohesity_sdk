# McmTenantSourceRegistration

Specifies a source registration for a given tenant.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_registration_id** | **str, none_type** | Specifies the id assigned to the entry. | [optional] 
**source_id** | **int, none_type** | Specifies the ID of the source on the cluster. | [optional] 
**environment** | **str, none_type** | Specifies the environment of the source. | [optional] 
**object_type** | **str, none_type** | Specifies the type of the object. | [optional] 
**is_root_source** | **bool, none_type** | Specifies whether or not this object is a root level source (registered directly rather than the child of a registered source). | [optional] 
**tenant_ids** | **[str, none_type]** | Specifies the tenants which have access to this object. | [optional] 
**account_id** | **str, none_type** | Specifies the account ID to which this source belongs. | [optional] 
**dmaas_tenant_id** | **str, none_type** | Specifies the DMaaS tenant ID to which this source belongs. | [optional] 
**cluster_id** | **int, none_type** | Specifies the ID of the cluster to which the source is registered. | [optional] 
**object_hash** | **str, none_type** | Specifies the object hash of the source. | [optional] 
**user_details** | [**User**](User.md) |  | [optional] 
**created_at_msecs** | **int, none_type** | Specifies the timestamp at which this entry was created in msecs. | [optional] 
**updated_at_msecs** | **int, none_type** | Specifies the timestamp at which this entry was updated in msecs. | [optional] 
**source_registration** | [**SourceRegistration**](SourceRegistration.md) |  | [optional] 
**enable_app_params** | [**[ObjectActionRequest]**](ObjectActionRequest.md) | Specifies the list of enable application params which have been performed on this source. | [optional] 
**credentials** | [**SourceRegistrationCredentials**](SourceRegistrationCredentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


