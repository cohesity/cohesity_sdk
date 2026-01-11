# DB2SourceRegistrationParams

Specifies parameters to register a DB2 source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **[str]** | Specifies the IPs/hostnames for the nodes forming the DB2 source cluster. | 
**profile_path** | **str** | Specifies file location of DB2 Profile path of the instance. | 
**script_dir** | **str** | Specifies the absolute path of scripts used to interact with the DB2 source. | 
**source_name** | **str** | Specifies user friendly unique name provided for registering DB2 source. | 
**username** | **str** | Specifies the username to access target DB2 entity. | 
**host_os_type** | **str, none_type** | Specifies the type of DB2 host. | [optional] 
**source_registration_arguments** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the source registration scripts. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


