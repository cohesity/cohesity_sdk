# HeliosAuditLogUser

Specifies user for helios audit log message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | Specifies user name. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log_user import HeliosAuditLogUser

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogUser from a JSON string
helios_audit_log_user_instance = HeliosAuditLogUser.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogUser.to_json())

# convert the object into a dict
helios_audit_log_user_dict = helios_audit_log_user_instance.to_dict()
# create an instance of HeliosAuditLogUser from a dict
helios_audit_log_user_from_dict = HeliosAuditLogUser.from_dict(helios_audit_log_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


