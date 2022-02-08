# UdaSourceRegistrationParams

Specifies parameters to register a Universal Data Adapter source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | Specifies the source type for Universal Data Adapter source. | 
**hosts** | **[str]** | Specifies the IPs/hostnames for the nodes forming the Universal Data Adapter source cluster. | 
**script_dir** | **str** | Specifies the absolute path of scripts used to interact with the Universal Data Adapter source. | 
**credentials** | [**UdaSourceRegistrationParamsCredentials**](UdaSourceRegistrationParamsCredentials.md) |  | [optional] 
**mount_view** | **bool, none_type** | Specifies if SMB/NFS view mounting should be enabled on source. Default value is false. | [optional] 
**view_params** | [**UdaSourceRegistrationParamsViewParams**](UdaSourceRegistrationParamsViewParams.md) |  | [optional] 
**source_registration_args** | **str, none_type** | Specifies custom arguments to be supplied to the source registration scripts. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


