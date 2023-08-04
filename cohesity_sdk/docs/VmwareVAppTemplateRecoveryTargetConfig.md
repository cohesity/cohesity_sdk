# VmwareVAppTemplateRecoveryTargetConfig

Specifies the target object parameters to recover VMware vApp templates.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**new_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the new destination Source configuration parameters where the vApp templates will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the Source configuration if vApp templates are being recovered to Original Source. If not specified, all the configuration parameters will be retained. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


