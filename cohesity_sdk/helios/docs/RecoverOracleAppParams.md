# RecoverOracleAppParams

Specifies the parameters to recover Oracle databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oracle_target_params** | [**OracleTargetParamsForRecoverOracleApp**](OracleTargetParamsForRecoverOracleApp.md) | Specifies the params for recovering to a oracle host. Provided oracle backup should be recovered to same type of target host. For Example: If you have oracle backup taken from a physical host then that should be recovered to physical host only. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_oracle_app_params import RecoverOracleAppParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleAppParams from a JSON string
recover_oracle_app_params_instance = RecoverOracleAppParams.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleAppParams.to_json())

# convert the object into a dict
recover_oracle_app_params_dict = recover_oracle_app_params_instance.to_dict()
# create an instance of RecoverOracleAppParams from a dict
recover_oracle_app_params_from_dict = RecoverOracleAppParams.from_dict(recover_oracle_app_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


