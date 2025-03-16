# CountByTier

CountByTier provides the disk count of each storage tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_count** | **int** | DiskCount is the disk number of the storage tier. | [optional] 
**storage_tier** | **str** | StorageTier is the type of StorageTier. StorageTierType represents the various values for the Storage Tier. &#39;kPCIeSSD&#39; indicates storage tier type of Pci Solid State Drive. &#39;kSATAHDD&#39; indicates storage tier type of SATA Solid State Drive. &#39;kSATAHDD&#39; indicates storage tier type of SATA Hard Disk Drive. &#39;kCLOUD&#39; indicates storage tier type of Cloud. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.count_by_tier import CountByTier

# TODO update the JSON string below
json = "{}"
# create an instance of CountByTier from a JSON string
count_by_tier_instance = CountByTier.from_json(json)
# print the JSON string representation of the object
print(CountByTier.to_json())

# convert the object into a dict
count_by_tier_dict = count_by_tier_instance.to_dict()
# create an instance of CountByTier from a dict
count_by_tier_from_dict = CountByTier.from_dict(count_by_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


