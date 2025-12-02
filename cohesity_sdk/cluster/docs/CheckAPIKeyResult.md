# CheckAPIKeyResult

Specifies the result after performing API key check for Primary Cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_api_key_valid** | **bool** | Specifies whether the API key is still valid. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.check_api_key_result import CheckAPIKeyResult

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAPIKeyResult from a JSON string
check_api_key_result_instance = CheckAPIKeyResult.from_json(json)
# print the JSON string representation of the object
print(CheckAPIKeyResult.to_json())

# convert the object into a dict
check_api_key_result_dict = check_api_key_result_instance.to_dict()
# create an instance of CheckAPIKeyResult from a dict
check_api_key_result_from_dict = CheckAPIKeyResult.from_dict(check_api_key_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


