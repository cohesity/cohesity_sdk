# MountUserCreds

Specify creds for mounting SMB share on the host

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_local_user** | **bool** | Specifies if the selected user is local user which is created on the cluster or a domain user | 
**sid** | **str** | Specifies the SID of the user selected. This should be in the correct format and should be referring the username passed. If passed wrongly then restore will fail. | 
**username** | **str** | Specifies the username to mount the SMB share. The specified user would only have the SMB access to the cloned view. | 
**domain_name** | **str, none_type** | Specifies the domain the user belongs to. Optional domain if a user from AD is selected. | [optional] 
**password** | **str, none_type** | Specifies the password to access the SMB share. Optional if domain user is selected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


