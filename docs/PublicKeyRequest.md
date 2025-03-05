# PublicKeyRequest

Specifies the parameters required to retrieve SSH public key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_type** | **str** | Specifies the workflow initiating the SSH connection. | 

## Example

```python
from cohesity_sdk.models.public_key_request import PublicKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublicKeyRequest from a JSON string
public_key_request_instance = PublicKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PublicKeyRequest.to_json())

# convert the object into a dict
public_key_request_dict = public_key_request_instance.to_dict()
# create an instance of PublicKeyRequest from a dict
public_key_request_from_dict = PublicKeyRequest.from_dict(public_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


