# RecoverAwsVmNewSourceConfig

Specifies the new destination Source configuration where the VMs will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the id of the parent source to recover the VMs. | 
**region** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the AWS region in which to deploy the VM. | 
**network_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the networking configuration to be applied to the recovered VMs. | 
**key_pair** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the pair of public and private key used to login into the VM | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


