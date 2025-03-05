# StoragePolicy

Specifies the storage policy of a Storage Domain.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aes_encryption_mode** | **str** | Specifies the encryption mode for a Storage Domain. | [optional] 
**app_marker_detection_enabled** | **bool** | Specifies whether app marker detection is enabled. When enabled, app markers will be removed from data and put in separate chunks. | [optional] 
**cloud_spill_vault_id** | **int** | Specifies the vault id assigned for cloud spill for a Storage Domain. | [optional] 
**compression_params** | [**CompressionParams**](CompressionParams.md) |  | [optional] 
**deduplication_compression_delay_secs** | **int** | Specifies the time in seconds when deduplication and compression of the Storage Domain starts. | [optional] 
**deduplication_params** | [**DeduplicationParams**](DeduplicationParams.md) |  | [optional] 
**encryption_type** | **str** | Specifies the encryption type for a Storage Domain. | [optional] 
**erasure_coding_params** | [**ErasureCodingParams**](ErasureCodingParams.md) |  | [optional] 
**num_disk_failures_tolerated** | **int** | Specifies the number of disk failures to tolerate for a Storage Domain. By default, this field is 1 for cluster with three or more nodes. If erasure coding is enabled, this field will be the same as numCodedStripes. | [optional] 
**num_node_failures_tolerated** | **int** | Specifies the number of node failures to tolerate for a Storage Domain. By default this field is replication factor minus 1 for replication chunk files and is the same as numCodedStripes for erasure coding chunk files. | [optional] 

## Example

```python
from cohesity_sdk.models.storage_policy import StoragePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePolicy from a JSON string
storage_policy_instance = StoragePolicy.from_json(json)
# print the JSON string representation of the object
print(StoragePolicy.to_json())

# convert the object into a dict
storage_policy_dict = storage_policy_instance.to_dict()
# create an instance of StoragePolicy from a dict
storage_policy_from_dict = StoragePolicy.from_dict(storage_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


