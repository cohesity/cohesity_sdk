# DataTransferInfo

Specifies the the details of network used in transferring the data from source account to Cohesity cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_private_network** | **bool, none_type** | Specifies whether to use private network or public network. | [optional] 
**use_protection_job_info** | **bool, none_type** | Specifies Whether to use private network info which was used in backup of VMs.This should be populated only for restore job. | [optional] 
**private_network_info_list** | [**[PrivateNetworkInfo]**](PrivateNetworkInfo.md) | Specifies Information required to create endpoints in private networks for all regions whose VMs are getting protected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


