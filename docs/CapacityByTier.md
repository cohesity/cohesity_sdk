# CapacityByTier

CapacityByTier provides the physical capacity in bytes of each storage tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_physical_capacity_bytes_tier** | **int** | maxPhysicalCapacityBytesTier is the maximum physical capacity in bytes of the storage tier. | [optional] 
**storage_tier** | **str** | StorageTier is the type of StorageTier. StorageTierType represents the various values for the Storage Tier. &#39;kPCIeSSD&#39; indicates storage tier type of Pci Solid State Drive. &#39;kSATAHDD&#39; indicates storage tier type of SATA Solid State Drive. &#39;kSATAHDD&#39; indicates storage tier type of SATA Hard Disk Drive. &#39;kCLOUD&#39; indicates storage tier type of Cloud. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.capacity_by_tier import CapacityByTier

# TODO update the JSON string below
json = "{}"
# create an instance of CapacityByTier from a JSON string
capacity_by_tier_instance = CapacityByTier.from_json(json)
# print the JSON string representation of the object
print(CapacityByTier.to_json())

# convert the object into a dict
capacity_by_tier_dict = capacity_by_tier_instance.to_dict()
# create an instance of CapacityByTier from a dict
capacity_by_tier_from_dict = CapacityByTier.from_dict(capacity_by_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


