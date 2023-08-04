# SyslogServer

Specifies information about syslog server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | The id of the syslog server. | [optional] 
**ip** | **str, none_type** | Specifies the IP address or hostname of the syslog server. | [optional] 
**port** | **int, none_type** | Specifies the port where the syslog server listens. | [optional] 
**protocol** | **str, none_type** | Specifies the protocol used to send the logs. | [optional] 
**name** | **str, none_type** | Specifies a unique name for the syslog server on the Cluster. | [optional] 
**enabled** | **bool, none_type** | Specifies whether to enable the syslog server on the Cluster. | [optional] 
**facility_list** | **[str]** | Send enabled syslog facilities related logs to logging server. | [optional] 
**program_name_list** | **[str]** | Send programes related logs to logging server. | [optional] 
**msg_pattern_list** | **[str]** | Send logs including the msg patterns to logging server. | [optional] 
**raw_msg_pattern_list** | **[str]** | Send logs including the msg patterns to logging server. | [optional] 
**is_tls_enabled** | **bool, none_type** | Specify whether to enable tls support. | [optional] 
**ca_certificate** | **str, none_type** | Syslog server CA certificate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


