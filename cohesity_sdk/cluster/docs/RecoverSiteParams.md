# RecoverSiteParams

Specifies the parameters to recover Microsoft Office 365 Sharepoint site.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectSiteParam], none_type**](ObjectSiteParam.md) | Specifies a list of site params associated with the objects to recover. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering the doc libs of a site, if one or more of doc libs failed to recover. Default value is false. | [optional] 
**recover_preservation_hold_library** | **bool, none_type** | Specifies whether to recover Preservation Hold Library associated with the Sites selected for restore. Default value is false. | [optional] 
**target_domain_object_id** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**target_site** | [**TargetSiteParam**](TargetSiteParam.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


