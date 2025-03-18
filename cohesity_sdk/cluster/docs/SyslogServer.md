# SyslogServer

Specifies information about syslog server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | Syslog server CA certificate. | [optional] 
**enabled** | **bool** | Specifies whether to enable the syslog server on the Cluster. | [optional] 
**facility_list** | **List[str]** | Send enabled syslog facilities related logs to logging server. | [optional] 
**id** | **int** | The id of the syslog server. | [optional] 
**ip** | **str** | Specifies the IP address or hostname of the syslog server. | [optional] 
**is_tls_enabled** | **bool** | Specify whether to enable tls support. | [optional] 
**msg_pattern_list** | **List[str]** | Send logs including the msg patterns to logging server. | [optional] 
**name** | **str** | Specifies a unique name for the syslog server on the Cluster. | [optional] 
**port** | **int** | Specifies the port where the syslog server listens. | [optional] 
**program_name_list** | **List[str]** | Send programes related logs to logging server. | [optional] 
**protocol** | **str** | Specifies the protocol used to send the logs. | [optional] 
**raw_msg_pattern_list** | **List[str]** | Send logs including the msg patterns to logging server. | [optional] 
**token_id** | **str** | TokenId used for filtering messages on a relay or collector | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.syslog_server import SyslogServer

# TODO update the JSON string below
json = "{}"
# create an instance of SyslogServer from a JSON string
syslog_server_instance = SyslogServer.from_json(json)
# print the JSON string representation of the object
print(SyslogServer.to_json())

# convert the object into a dict
syslog_server_dict = syslog_server_instance.to_dict()
# create an instance of SyslogServer from a dict
syslog_server_from_dict = SyslogServer.from_dict(syslog_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


