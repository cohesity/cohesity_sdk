# McmIBMStorageProtectClaimResponseParams

Specifies the response of claiming an IBM storage protect cluster to Helios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ca_chain** | **str, none_type** | Specifies the CA chain that is used to sign the cluster certificate. | [optional] 
**cluster_certificate** | **str, none_type** | Specifies the Cluster certificate. | [optional] 
**cluster_id** | **int, none_type** | Specifies the cluster ID. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation ID. | [optional] 
**cluster_name** | **str, none_type** | Specifies the cluster name. | [optional] 
**cluster_private_key** | **str, none_type** | Specifies the Cluster private key. | [optional] 
**helios_certificate** | **str, none_type** | Specifies the Helios certificate that can be used to authenticate api calls made from Helios to cluster. | [optional] 
**passphrase** | **str, none_type** | Specifies the passphrase (if used) to encrypt the cluster private key. | [optional] 
**sf_account_id** | **str, none_type** | Specifies the Salesforce account ID used to claim the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


