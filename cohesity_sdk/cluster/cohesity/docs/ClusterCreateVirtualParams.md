# ClusterCreateVirtualParams

Params for Virtual Edition Cluster Creation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_api_based_fetch** | **bool, none_type** | Specifies if API based GET should be enabled for cluster destroy params | [optional] 
**apps_subnet_ip** | **str, none_type** | Specifies the IP for apps subnet | [optional] 
**apps_subnet_ip_v6** | **str, none_type** | Specifies the IPv6 for apps subnet | [optional] 
**apps_subnet_mask** | **str, none_type** | Specifies the Mask for apps subnet | [optional] 
**apps_subnet_mask_v6** | **str, none_type** | Specifies the MaskV6 for apps subnet | [optional] 
**cluster_destroy_hmac_key** | **str, none_type** | Specifies HMAC secret key that will be used to validate OTP used for destroy request | [optional] 
**enable_cluster_destroy** | **bool, none_type** | Specifies if cluster destroy op is enabled on this cluster | [optional] 
**encryption_config** | [**EncryptionConfigurationParams**](EncryptionConfigurationParams.md) |  | [optional] 
**ip_preference** | **int, none_type** | Specifies IP preference | [optional] 
**metadata_fault_tolerance** | **int, none_type** | Specifies the metadata fault tolerance. | [optional] 
**node_configs** | [**[NodeConfigParams]**](NodeConfigParams.md) | Configuration of the nodes. | [optional] 
**trust_domain** | **str, none_type** | Specifies Trust Domain used for Service Identity | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


