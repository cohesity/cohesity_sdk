# SyslogServerStatus

Remote system logging server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the syslog server. | [optional] 
**is_reachable** | **bool** | Specify if the syslog server is reachable or not. | [optional] 
**message** | **str** | Description for current status. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.syslog_server_status import SyslogServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServerStatus from a JSON string
syslog_server_status_instance = SyslogServerStatus.from_json(json)
# print the JSON string representation of the object
print(SyslogServerStatus.to_json())

# convert the object into a dict
syslog_server_status_dict = syslog_server_status_instance.to_dict()
# create an instance of SyslogServerStatus from a dict
syslog_server_status_from_dict = SyslogServerStatus.from_dict(syslog_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


