# PublishHeliosAuditLogRequest

Request object for publishing helios audit logs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Specifies the entity type. | 
**action** | **str** | Specifies the action type of this audit log. | 
**details** | **str, none_type** | Specifies the change details of this audit log. | [optional] 
**entity_name** | **str, none_type** | Specifies the entity name. | [optional] 
**entity_id** | **str, none_type** | Specifies the entity id. | [optional] 
**ip** | **str, none_type** | Specifies the ip of user who made this audit log. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id who made this audit log. | [optional] 
**tenant_name** | **str, none_type** | Specifies the tenant name who made this audit log. | [optional] 
**original_tenant_id** | **str, none_type** | Specifies the original tenant id who made this audit log. | [optional] 
**original_tenant_name** | **str, none_type** | Specifies the original tenant name who made this audit log. | [optional] 
**previous_record** | **bool, date, datetime, dict, float, int, list, str, none_type** | Specifies the record before the action is invoked. This will be returned only if verbose audit is enabled.  | [optional] 
**new_record** | **bool, date, datetime, dict, float, int, list, str, none_type** | Specifies the record after the action is invoked. This will be returned only if verbose audit is enabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


