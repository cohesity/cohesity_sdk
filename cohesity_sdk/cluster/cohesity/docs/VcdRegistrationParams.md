# VcdRegistrationParams

Specifies parameters to register VMware vCloud director.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**vcenter_credential_info_list** | [**[VcenterCredentialInfo], none_type**](VcenterCredentialInfo.md) | Specifies the credentials information for all the vcenters in vcloud director. | 
**description** | **str, none_type** | Specifies the description of the source being registered. | [optional] 
**link_vms_across_vcenter** | **bool, none_type** | Specifies if the VM linking feature is enabled for the VCD. If enabled, migrated VMs present in the VCD which earlier belonged to some other VCD/Vcenter will be linked during EH refresh. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


