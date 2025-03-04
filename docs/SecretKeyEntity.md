# SecretKeyEntity

Specifies the new secret key instance generated for the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **str** | Specifies the new s3 secret key. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.secret_key_entity import SecretKeyEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SecretKeyEntity from a JSON string
secret_key_entity_instance = SecretKeyEntity.from_json(json)
# print the JSON string representation of the object
print(SecretKeyEntity.to_json())

# convert the object into a dict
secret_key_entity_dict = secret_key_entity_instance.to_dict()
# create an instance of SecretKeyEntity from a dict
secret_key_entity_from_dict = SecretKeyEntity.from_dict(secret_key_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


