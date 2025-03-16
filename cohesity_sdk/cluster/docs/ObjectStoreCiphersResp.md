# ObjectStoreCiphersResp

Specifies a list of enabled/disabled object store ciphers on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_ciphers** | **List[str]** | Disabled object store ciphers. | [optional] 
**enabled_ciphers** | **List[str]** | Enabled object store ciphers. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_store_ciphers_resp import ObjectStoreCiphersResp

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectStoreCiphersResp from a JSON string
object_store_ciphers_resp_instance = ObjectStoreCiphersResp.from_json(json)
# print the JSON string representation of the object
print(ObjectStoreCiphersResp.to_json())

# convert the object into a dict
object_store_ciphers_resp_dict = object_store_ciphers_resp_instance.to_dict()
# create an instance of ObjectStoreCiphersResp from a dict
object_store_ciphers_resp_from_dict = ObjectStoreCiphersResp.from_dict(object_store_ciphers_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


