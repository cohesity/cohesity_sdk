# HeliosAuditLogs

Specifies the helios audit logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_logs** | [**List[HeliosAuditLog]**](HeliosAuditLog.md) | Specifies a list of audit logs. | [optional] 
**count** | **int** | Specifies the total number of audit logs that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_logs import HeliosAuditLogs

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogs from a JSON string
helios_audit_logs_instance = HeliosAuditLogs.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogs.to_json())

# convert the object into a dict
helios_audit_logs_dict = helios_audit_logs_instance.to_dict()
# create an instance of HeliosAuditLogs from a dict
helios_audit_logs_from_dict = HeliosAuditLogs.from_dict(helios_audit_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


