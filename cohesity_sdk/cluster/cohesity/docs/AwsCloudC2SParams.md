# AwsCloudC2SParams

Specifies the parameters which are specific to AWS related External Targets with Cloud Type C2S.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **str, none_type** | Specifies agency of the External Target. | 
**base_url** | **str, none_type** | Specifies base url of the External Target. | 
**mission** | **str, none_type** | Specifies mission of the External Target | 
**role** | **str, none_type** | Specifies role of the External Target | 
**c2s_type** | **str, none_type** | Specifies C2S type of the External Target C2S or SC2S. C2S is for Top secrect Cloud Services. In case the type is not provided, default value is assumed as C2S. | [optional] 
**client_certificate** | **str, none_type** | Specifies client certificate of the External Target | [optional] 
**client_certificate_password** | **str, none_type** | Specifies client certificate password of the External Target | [optional] 
**client_private_key** | **str, none_type** | Specifies client private key of the External Target | [optional] 
**server_ca_trusted_certificate** | **str, none_type** | Specifies server CA trusted certificate of the External Target | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


