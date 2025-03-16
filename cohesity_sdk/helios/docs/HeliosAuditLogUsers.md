# HeliosAuditLogUsers

Specifies users for helios audit log message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_users** | [**List[HeliosAuditLogClusterUser]**](HeliosAuditLogClusterUser.md) | Specifies cluster users. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log_users import HeliosAuditLogUsers

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogUsers from a JSON string
helios_audit_log_users_instance = HeliosAuditLogUsers.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogUsers.to_json())

# convert the object into a dict
helios_audit_log_users_dict = helios_audit_log_users_instance.to_dict()
# create an instance of HeliosAuditLogUsers from a dict
helios_audit_log_users_from_dict = HeliosAuditLogUsers.from_dict(helios_audit_log_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


