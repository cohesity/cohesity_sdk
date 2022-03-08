# OracleProtectionGroupParams

Specifies the parameters to create Oracle Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[OracleProtectionGroupObjectParams], none_type**](OracleProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 
**persist_mountpoints** | **bool, none_type** | Specifies whether the mountpoints created while backing up Oracle DBs should be persisted. Defaults to true if value is null to handle the backward compatibility for the upgrade case. | [optional]  if omitted the server will use the default value of True
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


