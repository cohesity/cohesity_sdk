# HeliosAuditLog

Specifies an helios audit log message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type of this audit log. | [optional] 
**cluster_identifier** | **str** | Specifies the cluster identifier for this audit log. Format is of clusterId:clusterIncarnationId.  | [optional] 
**cluster_name** | **str** | Specifies the cluster name for this audtit log. | [optional] 
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
**service_context** | **str** | Specifies in which context in which the audit log was generated. | [optional] 
**source_type** | **str** | Specifies the source type for this audit log. | [optional] 
**tenant_id** | **str** | Specifies the tenant id who made this audit log. | [optional] 
**tenant_name** | **str** | Specifies the tenant name who made this audit log. | [optional] 
**timestamp_usecs** | **int** | Specifies a unix timestamp in micro seconds when the audit log was taken. | [optional] 
**username** | **str** | Specifies the username who made this audit log. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log import HeliosAuditLog

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLog from a JSON string
helios_audit_log_instance = HeliosAuditLog.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLog.to_json())

# convert the object into a dict
helios_audit_log_dict = helios_audit_log_instance.to_dict()
# create an instance of HeliosAuditLog from a dict
helios_audit_log_from_dict = HeliosAuditLog.from_dict(helios_audit_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


