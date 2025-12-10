# AzureTargetParamsForRecoverAzureEntraId

Specifies the parameters for an Azure recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_password_on_sign_in** | **bool** | Specifies Whether to force changing password on next sign in. Applies for only user type | [optional] 
**default_password** | **str** | Specifies the default password to be set in case users are recovered. | [optional] 
**is_container_member_recovery** | **bool** | Specifies whether recovery should recover all the members of a selected object. Applies for Admin Unit, Group and Dir Roles | [optional] 
**is_license_overwrite** | **bool** | If true, licenses are restored in overwrite mode (i.e. any license assigned *after* restore point is removed). For example, if user U1 has licenses L1 and L2 in restore point (in selected snapshot), but the same user has licenses L1 and L3 in live AAD, license assignment of L2 is restored and license assignment of L3 is removed in overwrite-mode while restoring U1. If this field is false or nil, license assignment is restored in merge-mode. In merge-mode, license assignment of L2 is restored and license assignment of L3 is not removed. | [optional] 
**is_relation_overwrite** | **bool** | If true, relationships are restored in overwrite mode (i.e. any relationship created *after* restore point is deleted). For example, if user U1 is member of G1 and G2 in restore point (in selected snapshot), but the same user is member of G1 and G3 in live AAD, membership of G2 is restored and membership of G3 is removed in overwrite-mode while restoring U1. If this field is false, relationship is restored in merge-mode. In merge-mode, membership of G2 is restored but membership of G3 is not removed. | [optional] 
**recovery_type** | **str** | Specifies the recovery type for the selected azure entra id recoverable object. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_azure_entra_id import AzureTargetParamsForRecoverAzureEntraId

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverAzureEntraId from a JSON string
azure_target_params_for_recover_azure_entra_id_instance = AzureTargetParamsForRecoverAzureEntraId.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverAzureEntraId.to_json())

# convert the object into a dict
azure_target_params_for_recover_azure_entra_id_dict = azure_target_params_for_recover_azure_entra_id_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverAzureEntraId from a dict
azure_target_params_for_recover_azure_entra_id_from_dict = AzureTargetParamsForRecoverAzureEntraId.from_dict(azure_target_params_for_recover_azure_entra_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


