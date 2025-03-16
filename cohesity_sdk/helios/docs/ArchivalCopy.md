# ArchivalCopy

Specifies the information about archival snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target** | [**ArchivalTarget**](ArchivalTarget.md) |  | [optional] 
**creation_time_usecs** | **int** | Specifies the creation time of archival snapshot. | [optional] 
**global_vault_id** | **str** | Specifies the global vault id of the archival snapshot. | [optional] 
**is_r_paas** | **bool** | Specifies whether this archival location is RPaas. | [optional] 
**rpaas_region** | **str** | If the location is RPaas then this specifies the region. | [optional] 
**snapshot_id** | **str** | Snapshot id of the snapshot corresponding to the archival copy of this backup run. | [optional] 
**status** | **str** | Specifies the status of the archival snapshot. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.archival_copy import ArchivalCopy

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalCopy from a JSON string
archival_copy_instance = ArchivalCopy.from_json(json)
# print the JSON string representation of the object
print(ArchivalCopy.to_json())

# convert the object into a dict
archival_copy_dict = archival_copy_instance.to_dict()
# create an instance of ArchivalCopy from a dict
archival_copy_from_dict = ArchivalCopy.from_dict(archival_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


