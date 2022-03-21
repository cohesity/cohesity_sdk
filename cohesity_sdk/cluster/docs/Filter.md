# Filter

Specifies the filter details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_string** | **str, none_type** | Specifies the filter string using wildcard supported strings or regular expressions. | [optional] 
**is_regular_expression** | **bool, none_type** | Specifies whether the provided filter string is a regular expression or not. This needs to be explicitly set to true if user is trying to filter by regular expressions. Not providing this value in case of regular expression can result in unintended results. The default value is assumed to be false. | [optional]  if omitted the server will use the default value of False

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


