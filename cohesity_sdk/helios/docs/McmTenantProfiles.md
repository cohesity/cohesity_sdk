# McmTenantProfiles

Specifies tenant profiles for a logged in user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sf_account_id** | **str, none_type** | Specifies the Salesforce account ID of this account. | [optional] 
**user_sid** | **str, none_type** | Specifies the sid of the logged in user. | [optional] 
**is_floating_user** | **bool, none_type** | Specifies whether or not this is a floating SSO user. | [optional] 
**roles** | **[str]** | Specifies the roles of the user. | [optional] 
**group_sids** | **[str]** | Specifies the sids of the groups the user belongs to. | [optional] 
**clusters** | [**[McmClusterIdentifier], none_type**](McmClusterIdentifier.md) | Specifies the list of clusters owned by this account id. | [optional] 
**tenant_profiles** | [**[McmTenantProfile], none_type**](McmTenantProfile.md) | Specifies the list of tenant profiles associated to this account if any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


