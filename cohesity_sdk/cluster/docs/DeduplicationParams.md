# DeduplicationParams

Specifies parameters for deduplication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether deduplication is enabled on this Storage Domain. If enabled, cohesity cluster will eliminate duplicate blocks and thus reducing the amount of storage space. | [optional] 
**inline_enabled** | **bool** | Specifies if inline deduplication is enabled. This field is appliciable only if deduplicationEnabled is set to true. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.deduplication_params import DeduplicationParams

# TODO update the JSON string below
json = "{}"
# create an instance of DeduplicationParams from a JSON string
deduplication_params_instance = DeduplicationParams.from_json(json)
# print the JSON string representation of the object
print(DeduplicationParams.to_json())

# convert the object into a dict
deduplication_params_dict = deduplication_params_instance.to_dict()
# create an instance of DeduplicationParams from a dict
deduplication_params_from_dict = DeduplicationParams.from_dict(deduplication_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


