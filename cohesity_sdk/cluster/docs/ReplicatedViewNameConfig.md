# ReplicatedViewNameConfig

Specifies an object protected by a View Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_view_id** | **int, none_type** | Specifies the ID of the protected view. | 
**use_same_view_name** | **bool, none_type** | Specifies if the remote view name to be kept is same as the source view name. If this field is true, viewName field will be ignored. | [optional] 
**view_name** | **str, none_type** | Specifies the name of the remote view. This field is only used when useSameViewName is false. If useSameViewName is true, this field is not used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


