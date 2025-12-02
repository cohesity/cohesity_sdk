# APIKeyParams

Specifies the API key authentication method parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Specifies the API key to access the external target. | 

## Example

```python
from cohesity_sdk.cluster.models.api_key_params import APIKeyParams

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyParams from a JSON string
api_key_params_instance = APIKeyParams.from_json(json)
# print the JSON string representation of the object
print(APIKeyParams.to_json())

# convert the object into a dict
api_key_params_dict = api_key_params_instance.to_dict()
# create an instance of APIKeyParams from a dict
api_key_params_from_dict = APIKeyParams.from_dict(api_key_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


