# McmCohesionClaimResponseParams

Specifies the response of claiming a Cohesion Appliance to Helios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliance_id** | **str, none_type** | Unique id of the cohesion appliance with AWS | [optional] 
**appliance_name** | **str, none_type** | Specifies the name of the cohesion appliance. | [optional] 
**ca_chain** | **str, none_type** | Specifies the CA chain that is used to sign the Cohesion Appliance certificate. | [optional] 
**certificate** | **str, none_type** | Specifies the Cohesion Appliance certificate. | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster id of the appliance. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id of the appliance. | [optional] 
**helios_certificate** | **str, none_type** | Specifies the Helios certificate that can be used to authenticate api calls made from Helios to Cohesion Appliance | [optional] 
**passphrase** | **str, none_type** | Specifies the passphrase (if used) to encrypt the Cohesion Appliance private key. | [optional] 
**private_key** | **str, none_type** | Specifies the Cohesion Appliance private key. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


