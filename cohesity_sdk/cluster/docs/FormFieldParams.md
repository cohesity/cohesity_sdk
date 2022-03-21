# FormFieldParams

Parameters to specify a form field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Id to identify the form field. This is also be used for assigning component html ids which can be leveraged for writing automation against the form field. | [optional] 
**label** | **str, none_type** | Label to be shown on the UI screen | [optional] 
**key** | **str, none_type** | Key against which the form field value will be returned | [optional] 
**type** | **str, none_type** | Type of the form field. Available types are &#39;string&#39;, &#39;password&#39;, &#39;number&#39;, &#39;boolean&#39;, &#39;radioGroup&#39; | [optional] 
**string_config** | [**StringFormFieldParams**](StringFormFieldParams.md) |  | [optional] 
**password_config** | [**PasswordFormFieldParams**](PasswordFormFieldParams.md) |  | [optional] 
**number_config** | [**NumberFormFieldParams**](NumberFormFieldParams.md) |  | [optional] 
**boolean_config** | [**BooleanFormFieldParams**](BooleanFormFieldParams.md) |  | [optional] 
**radio_group_config** | [**RadioGroupFormFieldParams**](RadioGroupFormFieldParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


