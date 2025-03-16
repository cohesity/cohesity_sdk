# CommonTieringPolicy

Specifies the common tiering params between uptiering and downtiering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_audit_logging** | **bool** | Specifies whether to audit log the file tiering activity. | [optional] [default to False]
**file_path** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**file_size** | [**FileSizePolicy**](FileSizePolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_tiering_policy import CommonTieringPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of CommonTieringPolicy from a JSON string
common_tiering_policy_instance = CommonTieringPolicy.from_json(json)
# print the JSON string representation of the object
print(CommonTieringPolicy.to_json())

# convert the object into a dict
common_tiering_policy_dict = common_tiering_policy_instance.to_dict()
# create an instance of CommonTieringPolicy from a dict
common_tiering_policy_from_dict = CommonTieringPolicy.from_dict(common_tiering_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


