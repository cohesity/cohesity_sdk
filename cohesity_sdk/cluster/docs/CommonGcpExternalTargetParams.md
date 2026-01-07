# CommonGcpExternalTargetParams

Specifies the common parameters which are specific to GCP related External Targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str, none_type** | Specifies the bucket name of the external target. | 
**project_id** | **str, none_type** | Specifies the project Id of the external target. | 
**authentication_method** | [**GCPAuthenticationMethodsParams**](GCPAuthenticationMethodsParams.md) |  | [optional] 
**client_email_address** | **str, none_type** | Specifies the client email address of the external target. This field is being deprecated, please use authenticationMethod instead. | [optional] 
**client_private_key** | **str, none_type** | Specifies the client private key of the external target. This field is being deprecated, please use authenticationMethod instead. | [optional] 
**region** | **str, none_type** | Specifies the Google Cloud region where the storage bucket is located (e.g., &#39;us-central1&#39;, &#39;europe-west1&#39;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


