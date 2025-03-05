# CiphersResp

Specifies a list of enabled/disabled ciphers on the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_ciphers** | **List[str]** | Disabled ciphers. | [optional] 
**enabled_ciphers** | **List[str]** | Enabled ciphers. | [optional] 

## Example

```python
from cohesity_sdk.models.ciphers_resp import CiphersResp

# TODO update the JSON string below
json = "{}"
# create an instance of CiphersResp from a JSON string
ciphers_resp_instance = CiphersResp.from_json(json)
# print the JSON string representation of the object
print(CiphersResp.to_json())

# convert the object into a dict
ciphers_resp_dict = ciphers_resp_instance.to_dict()
# create an instance of CiphersResp from a dict
ciphers_resp_from_dict = CiphersResp.from_dict(ciphers_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


