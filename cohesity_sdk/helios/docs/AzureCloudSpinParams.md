# AzureCloudSpinParams

Specifies various resources when converting and deploying a VM to Azure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_set_id** | **int** | Specifies the availability set. | [optional] 
**network_resource_group_id** | **int** | Specifies id of the resource group for the selected virtual network. | [optional] 
**resource_group_id** | **int** | Specifies id of the Azure resource group. Its value is globally unique within Azure. | [optional] 
**storage_account_id** | **int** | Specifies id of the storage account that will contain the storage container within which we will create the blob that will become the VHD disk for the cloned VM. | [optional] 
**storage_container_id** | **int** | Specifies id of the storage container within the above storage account. | [optional] 
**storage_resource_group_id** | **int** | Specifies id of the resource group for the selected storage account. | [optional] 
**temp_vm_resource_group_id** | **int** | Specifies id of the temporary Azure resource group. | [optional] 
**temp_vm_storage_account_id** | **int** | Specifies id of the temporary VM storage account that will contain the storage container within which we will create the blob that will become the VHD disk for the cloned VM. | [optional] 
**temp_vm_storage_container_id** | **int** | Specifies id of the temporary VM storage container within the above storage account. | [optional] 
**temp_vm_subnet_id** | **int** | Specifies Id of the temporary VM subnet within the above virtual network. | [optional] 
**temp_vm_virtual_network_id** | **int** | Specifies Id of the temporary VM Virtual Network. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.azure_cloud_spin_params import AzureCloudSpinParams

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCloudSpinParams from a JSON string
azure_cloud_spin_params_instance = AzureCloudSpinParams.from_json(json)
# print the JSON string representation of the object
print(AzureCloudSpinParams.to_json())

# convert the object into a dict
azure_cloud_spin_params_dict = azure_cloud_spin_params_instance.to_dict()
# create an instance of AzureCloudSpinParams from a dict
azure_cloud_spin_params_from_dict = AzureCloudSpinParams.from_dict(azure_cloud_spin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


