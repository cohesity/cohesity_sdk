# OracleEnvJobParams

Specifies job parameters applicable for all 'kOracle' Environment type Protection Sources in a Protection Job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persist_mountpoints** | **bool, none_type** | Specifies whether the mountpoints created while backing up Oracle DBs should be persisted. Note: This parameter is for the entire Job. For overriding persistence of mountpoints for a subset of Oracle hosts within the job, refer OracleSourceParams. | [optional] 
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


