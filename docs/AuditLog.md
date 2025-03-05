# AuditLog

Specifies an audit log message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type of this audit log. | [optional] 
**details** | **str** | Specifies the change details of this audit log. | [optional] 
**domain** | **str** | Specifies the domain of user who made this audit log. | [optional] 
**entity_name** | **str** | Specifies the entity name. | [optional] 
**entity_type** | **str** | Specifies the entity type. | [optional] 
**ip** | **str** | Specifies the ip of user who made this audit log. | [optional] 
**is_impersonation** | **bool** | Specifies if the action is made through impersonation. | [optional] 
**new_record** | **str** | Specifies the record after the action is invoked. This will be returned only if verbose audit is enabled.  | [optional] 
**original_tenant_id** | **str** | Specifies the original tenant id who made this audit log. | [optional] 
**original_tenant_name** | **str** | Specifies the original tenant name who made this audit log. | [optional] 
**previous_record** | **str** | Specifies the record before the action is invoked. This will be returned only if verbose audit is enabled.  | [optional] 
**tenant_id** | **str** | Specifies the tenant id who made this audit log. | [optional] 
**tenant_name** | **str** | Specifies the tenant name who made this audit log. | [optional] 
**timestamp_usecs** | **int** | Specifies a unix timestamp in micro seconds when the audit log was taken. | [optional] 
**username** | **str** | Specifies the username who made this audit log. | [optional] 

## Example

```python
from cohesity_sdk.models.audit_log import AuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLog from a JSON string
audit_log_instance = AuditLog.from_json(json)
# print the JSON string representation of the object
print(AuditLog.to_json())

# convert the object into a dict
audit_log_dict = audit_log_instance.to_dict()
# create an instance of AuditLog from a dict
audit_log_from_dict = AuditLog.from_dict(audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


