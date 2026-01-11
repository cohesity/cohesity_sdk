# KubernetesAutoProtectConfig

Specifies the parameters to auto protect the source after registration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default_auto_protected** | **bool** | Specifies if entire source should be auto protected after registration. Default: False | 
**policy_id** | **str** | Specifies the protection policy to auto protect the source with. | 
**error_message** | **str, none_type** | Specifies the error message in case source registration is successful but protection job creation fails | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group Id after it is successfully created | [optional] 
**storage_domain_id** | **int** | Specifies the storage domain id for the protection job | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


