# VerifyTotpRequest

Holds the Totp code to be verified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totp_code** | **str** | Specifies the Totp code. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.verify_totp_request import VerifyTotpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTotpRequest from a JSON string
verify_totp_request_instance = VerifyTotpRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyTotpRequest.to_json())

# convert the object into a dict
verify_totp_request_dict = verify_totp_request_instance.to_dict()
# create an instance of VerifyTotpRequest from a dict
verify_totp_request_from_dict = VerifyTotpRequest.from_dict(verify_totp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


