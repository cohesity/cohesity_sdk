# SuccessResp

Specifies the firewall profile names to be removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the response message. | 

## Example

```python
from cohesity_sdk.helios.models.success_resp import SuccessResp

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessResp from a JSON string
success_resp_instance = SuccessResp.from_json(json)
# print the JSON string representation of the object
print(SuccessResp.to_json())

# convert the object into a dict
success_resp_dict = success_resp_instance.to_dict()
# create an instance of SuccessResp from a dict
success_resp_from_dict = SuccessResp.from_dict(success_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


