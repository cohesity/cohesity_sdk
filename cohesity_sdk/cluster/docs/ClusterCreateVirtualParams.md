# ClusterCreateVirtualParams

Params for Virtual Edition Cluster Creation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_api_based_fetch** | **bool** | Specifies if API based GET should be enabled for cluster destroy params | [optional] 
**apps_subnet_ip** | **str** | Specifies the IP for apps subnet | [optional] 
**apps_subnet_ip_v6** | **str** | Specifies the IPv6 for apps subnet | [optional] 
**apps_subnet_mask** | **str** | Specifies the Mask for apps subnet | [optional] 
**apps_subnet_mask_v6** | **str** | Specifies the MaskV6 for apps subnet | [optional] 
**cluster_destroy_hmac_key** | **str** | Specifies HMAC secret key that will be used to validate OTP used for destroy request | [optional] 
**enable_cluster_destroy** | **bool** | Specifies if cluster destroy op is enabled on this cluster | [optional] 
**encryption_config** | [**EncryptionConfigurationParams**](EncryptionConfigurationParams.md) |  | [optional] 
**ip_preference** | **int** | Specifies IP preference | [optional] 
**metadata_fault_tolerance** | **int** | Specifies the metadata fault tolerance. | [optional] 
**node_configs** | [**List[NodeConfigParams]**](NodeConfigParams.md) | Configuration of the nodes. | [optional] 
**trust_domain** | **str** | Specifies Trust Domain used for Service Identity | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_create_virtual_params import ClusterCreateVirtualParams

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCreateVirtualParams from a JSON string
cluster_create_virtual_params_instance = ClusterCreateVirtualParams.from_json(json)
# print the JSON string representation of the object
print(ClusterCreateVirtualParams.to_json())

# convert the object into a dict
cluster_create_virtual_params_dict = cluster_create_virtual_params_instance.to_dict()
# create an instance of ClusterCreateVirtualParams from a dict
cluster_create_virtual_params_from_dict = ClusterCreateVirtualParams.from_dict(cluster_create_virtual_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


