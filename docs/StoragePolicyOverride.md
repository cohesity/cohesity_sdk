# StoragePolicyOverride

Specifies if inline deduplication and compression settings inherited from Storage Domain (View Box) should be disabled for this View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_dedup** | **bool** | If it is set to true, we would disable dedup for writes made in this view irrespective of the view box&#39;s storage policy. | [optional] 
**disable_inline_dedup_and_compression** | **bool** | If false, the inline deduplication and compression settings inherited from the Storage Domain (View Box) apply to this View. If true, both inline deduplication and compression are disabled for this View. This can only be set to true if inline deduplication is set for the Storage Domain (View Box). | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.storage_policy_override import StoragePolicyOverride

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePolicyOverride from a JSON string
storage_policy_override_instance = StoragePolicyOverride.from_json(json)
# print the JSON string representation of the object
print(StoragePolicyOverride.to_json())

# convert the object into a dict
storage_policy_override_dict = storage_policy_override_instance.to_dict()
# create an instance of StoragePolicyOverride from a dict
storage_policy_override_from_dict = StoragePolicyOverride.from_dict(storage_policy_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


