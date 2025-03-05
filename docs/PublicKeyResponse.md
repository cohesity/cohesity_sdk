# PublicKeyResponse

Specifies the public key information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** | Specifies the SSH public key. | [optional] 

## Example

```python
from cohesity_sdk.models.public_key_response import PublicKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKeyResponse from a JSON string
public_key_response_instance = PublicKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PublicKeyResponse.to_json())

# convert the object into a dict
public_key_response_dict = public_key_response_instance.to_dict()
# create an instance of PublicKeyResponse from a dict
public_key_response_from_dict = PublicKeyResponse.from_dict(public_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


