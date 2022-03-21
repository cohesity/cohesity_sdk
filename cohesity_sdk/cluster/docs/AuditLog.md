# AuditLog

Specifies an audit log message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str, none_type** | Specifies the change details of this audit log. | [optional] 
**username** | **str, none_type** | Specifies the username who made this audit log. | [optional] 
**domain** | **str, none_type** | Specifies the domain of user who made this audit log. | [optional] 
**entity_name** | **str, none_type** | Specifies the entity name. | [optional] 
**entity_type** | **str, none_type** | Specifies the entity type. | [optional] 
**action** | **str, none_type** | Specifies the action type of this audit log. | [optional] 
**timestamp_usecs** | **int, none_type** | Specifies a unix timestamp in micro seconds when the audit log was taken. | [optional] 
**ip** | **str, none_type** | Specifies the ip of user who made this audit log. | [optional] 
**is_impersonation** | **bool, none_type** | Specifies if the action is made through impersonation. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id who made this audit log. | [optional] 
**tenant_name** | **str, none_type** | Specifies the tenant name who made this audit log. | [optional] 
**original_tenant_id** | **str, none_type** | Specifies the original tenant id who made this audit log. | [optional] 
**original_tenant_name** | **str, none_type** | Specifies the original tenant name who made this audit log. | [optional] 
**previous_record** | **str, none_type** | Specifies the record before the action is invoked. This will be returned only if verbose audit is enabled.  | [optional] 
**new_record** | **str, none_type** | Specifies the record after the action is invoked. This will be returned only if verbose audit is enabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


