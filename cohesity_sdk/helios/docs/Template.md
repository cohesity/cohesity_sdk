# Template

Description of the view template.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies an id of the view template. | [optional] [readonly] 
**name** | **str, none_type** | Specifies the name of the view template. | [optional] 
**dedup** | **bool, none_type** | Specifies whether to enable dedup in storage domain. | [optional] 
**compress** | **bool, none_type** | Specifies whether to enable compression in storage domain. | [optional] 
**is_default** | **bool, none_type** | Specifies if the tempate is custom or static. | [optional] [readonly] 
**default_template_name** | **str, none_type** | Used for uniquely indentifying a default template. | [optional] [readonly] 
**view_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the parameters which is used to create the view.   No field is required. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


