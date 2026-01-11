# AuthenticationMethod

Specifies the authentication method for IBMCOS APIs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str, none_type** | Specifies the authentication type for IBMCOS APIs. | 
**api_key** | **str, none_type** | Specifies the API key if the authenticationType is kApiKey. | [optional] 
**tenant_crn** | **str, none_type** | Specifies the teneant CRN if the authenticationType is kTrustedProfileWithS2SPolicy. | [optional] 
**trusted_profile_id** | **str, none_type** | Specifies the trusted profile id if the authenticationType is kTrustedProfile. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


