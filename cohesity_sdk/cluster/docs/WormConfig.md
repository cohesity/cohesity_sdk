# WormConfig

Specifies WORM related configs for a LSU. Once enabled, WORM cannot be removed. Any view created on this LSU will inherit these configs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_retention_secs** | **int, none_type** | Specifies max retention period in seconds. It must be greater than or equal to &#x60;min_retention_secs&#x60;. | [optional] 
**min_retention_secs** | **int, none_type** | Specifies min retention period in seconds. It must be greater than 0. | [optional] 
**mode** | **str, none_type** | Specifies WORM mode. It can be set to either &#39;Enterprise&#39; or &#39;Compliance&#39;. If mode is set to &#39;Compliance&#39;, it cannot be changed later. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


