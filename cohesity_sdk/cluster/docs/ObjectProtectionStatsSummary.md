# ObjectProtectionStatsSummary

Specifies the count and size of protected and unprotected objects for a given source environment/protection environment type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_protected_count** | **int** | Specifies the count of protected leaf objects which were deleted from the source after being protected. | [optional] 
**environment** | **str** | Specifies the source environment of the object. | [optional] 
**protected_count** | **int** | Specifies the count of the protected leaf objects. | [optional] 
**protected_size_bytes** | **int** | Specifies the protected logical size in bytes. | [optional] 
**protection_env_type** | **str** | Specifies the protection environment type. | [optional] 
**unprotected_count** | **int** | Specifies the count of the unprotected leaf objects. | [optional] 
**unprotected_size_bytes** | **int** | Specifies the unprotected logical size in bytes. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_protection_stats_summary import ObjectProtectionStatsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectProtectionStatsSummary from a JSON string
object_protection_stats_summary_instance = ObjectProtectionStatsSummary.from_json(json)
# print the JSON string representation of the object
print(ObjectProtectionStatsSummary.to_json())

# convert the object into a dict
object_protection_stats_summary_dict = object_protection_stats_summary_instance.to_dict()
# create an instance of ObjectProtectionStatsSummary from a dict
object_protection_stats_summary_from_dict = ObjectProtectionStatsSummary.from_dict(object_protection_stats_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


