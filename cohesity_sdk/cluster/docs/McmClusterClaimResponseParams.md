# McmClusterClaimResponseParams

Specifies the response of claiming a cluster to Helios.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] 
**cluster_name** | **str, none_type** | Specifies the cluster name. | [optional] 
**sf_account_id** | **str, none_type** | Specifies the Salesforce account id used to claim the cluster. | [optional] 
**cluster_certificate** | **str, none_type** | Specifies the Cluster certificate. | [optional] 
**cluster_private_key** | **str, none_type** | Specifies the Cluster private key. | [optional] 
**passphrase** | **str, none_type** | Specifies the passphrase (if used) to encrypt the cluster private key. | [optional] 
**cluster_ca_chain** | **str, none_type** | Specifies the CA chain that is used to sign the Cluster certificate. | [optional] 
**helios_certificate** | **str, none_type** | Specifies the Helios certificate that can be used to authenticate api calls made from Helios to cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


