# RecoverViewToViewFilesTargetParams

Specifies the params of the View recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_view** | **bool** | Specifies the parameter whether the recovery should be performed to a new or the original View target. | 
**new_view_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the new destination View configuration parameters where the files will be recovered. This is mandatory if recoverToNewView is set to true. | [optional] 
**original_view_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the View configuration if files are being recovered to original View. If not specified, all the configuration parameters will be retained. | [optional] 
**view_id** | **int, none_type** | Specifies the ID of the view. | [optional] 
**view_name** | **str, none_type** | Specifies the name of the new view that&#39;s the target for recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


