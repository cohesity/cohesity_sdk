# FilerLifecycleRuleFilter

Specifies the filter used to identify files that a Lifecycle Rule applies to.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_extensions** | **[str], none_type** | Specifies the file&#39;s selection based on their extension. Eg: .pdf, .txt, etc. Note: Provide extensions here with the initial &#39;.&#39; character, example .pdf and not pdf. Extensions are case-insensitive, i.e. .pdf extension in filter will delete all files have .pdf, .PDF, .pDF, etc. | [optional] 
**file_size** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies the file&#39;s selection based on their size. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


