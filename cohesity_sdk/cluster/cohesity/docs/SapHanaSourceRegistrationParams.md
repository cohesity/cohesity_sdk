# SapHanaSourceRegistrationParams

Specifies parameters to register a SAP HANA source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **[str]** | Specifies the IPs/hostnames for the nodes forming the SAP HANA source cluster. | 
**script_dir** | **str** | Specifies the absolute path of scripts used to interact with the SAP HANA source. | 
**source_name** | **str** | Specifies user friendly name for the source. | 
**backint_protocol_version** | **str, none_type** | Backint protocol version to be used during backup/restore. | [optional]  if omitted the server will use the default value of "1.0"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


