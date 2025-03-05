# SyslogAuditTag

Cohesity audit tag name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_audit** | **str** | Alert audit tagging name. | [optional] 
**cluster_audit** | **str** | Cluster audit tagging name. | [optional] 
**data_protection_events_audit** | **str** | Data protection events audit tagging name. | [optional] 
**filer_audit** | **str** | Filer audit tagging name. | [optional] 

## Example

```python
from cohesity_sdk.models.syslog_audit_tag import SyslogAuditTag

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogAuditTag from a JSON string
syslog_audit_tag_instance = SyslogAuditTag.from_json(json)
# print the JSON string representation of the object
print(SyslogAuditTag.to_json())

# convert the object into a dict
syslog_audit_tag_dict = syslog_audit_tag_instance.to_dict()
# create an instance of SyslogAuditTag from a dict
syslog_audit_tag_from_dict = SyslogAuditTag.from_dict(syslog_audit_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


