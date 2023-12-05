# RecoverSiteParams

Specifies the parameters to recover Microsoft Office 365 Sharepoint site.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[ObjectSiteParam], none_type**](ObjectSiteParam.md) | Specifies a list of site params associated with the objects to recover. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering the doc libs of a site, if one or more of doc libs failed to recover. Default value is false. | [optional] 
**target_domain_object_id** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the object id of the target domain in case of full recovery of a site to a target domain. | [optional] 
**target_site** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the target Site to recover to. If not specified, the objects will be recovered to original location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


