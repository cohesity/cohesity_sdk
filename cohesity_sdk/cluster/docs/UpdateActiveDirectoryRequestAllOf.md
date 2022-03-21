# UpdateActiveDirectoryRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_admin_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params of a user with administrative privilege of this Active Directory. This field is mandatory if machine accounts are updated. | [optional] 
**overwrite_machine_accounts** | **bool, none_type** | Specifies if specified machine accounts should overwrite existing machine accounts. | [optional] 
**id_mapping_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the params of the user id mapping info of an Active Directory. | [optional] 
**transitive_ad_trust_level_limit** | **int, none_type** | Specifies level of transitive Active Directory trust domains to be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


