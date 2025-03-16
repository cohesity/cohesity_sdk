# SyslogServers

Specifies the list of syslog servers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syslog_servers** | [**List[SyslogServer]**](SyslogServer.md) | Specifies the list of syslog servers. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.syslog_servers import SyslogServers

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServers from a JSON string
syslog_servers_instance = SyslogServers.from_json(json)
# print the JSON string representation of the object
print(SyslogServers.to_json())

# convert the object into a dict
syslog_servers_dict = syslog_servers_instance.to_dict()
# create an instance of SyslogServers from a dict
syslog_servers_from_dict = SyslogServers.from_dict(syslog_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


