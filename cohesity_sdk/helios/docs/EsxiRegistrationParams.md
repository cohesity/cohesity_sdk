# EsxiRegistrationParams

Specifies parameters to register VMware ESXi host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**description** | **str** | Specifies the description of the source being registered. | [optional] 
**endpoint** | **str** | Specifies the endpoint IPaddress, URL or hostname of the host. | 
**data_store_params** | [**List[DatastoreParams]**](DatastoreParams.md) | Specifies the datastore specific params. | [optional] 
**max_concurrent_streams** | **int** | If this value is &gt; 0 and the number of streams concurrently active on a datastore is equal to it, then any further requests to access the datastore would be denied until the number of active streams reduces. This applies for all the datastores in the specified host. | [optional] 
**min_free_datastore_space_for_backup_gb** | **int** | Specifies the minimum free space (in GB) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 
**min_free_datastore_space_for_backup_percentage** | **int** | Specifies the minimum free space (in percentage) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.esxi_registration_params import EsxiRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of EsxiRegistrationParams from a JSON string
esxi_registration_params_instance = EsxiRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(EsxiRegistrationParams.to_json())

# convert the object into a dict
esxi_registration_params_dict = esxi_registration_params_instance.to_dict()
# create an instance of EsxiRegistrationParams from a dict
esxi_registration_params_from_dict = EsxiRegistrationParams.from_dict(esxi_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


