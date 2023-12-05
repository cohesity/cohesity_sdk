# UdaConnectorConfigParams

Specifies the request parameters to create/update a new UDA connector config.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_config** | **str, none_type** | Specifies the index config as json string. | [optional] 
**os_specific_config** | [**[UdaOSSpecificConfigParams]**](UdaOSSpecificConfigParams.md) | Specifies operating system specific configuration. | [optional] 
**replace** | **bool, none_type** | If true, any existing connector config with the the same ID is replaced if it exists. | [optional] 
**ui_translation_config** | [**[UdaLocaleSpecificTranslations]**](UdaLocaleSpecificTranslations.md) | Specifies the translation messages for various locales. It maps locale name to their respective translation json strings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


