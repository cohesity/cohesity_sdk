# VerifyTotpResult

Result of verifying totp code for support user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies message of otp verification result. | [optional] 
**success** | **bool** | Specifies whether or not verification of totp code is success. | [optional] [default to False]

## Example

```python
from cohesity_sdk.helios.models.verify_totp_result import VerifyTotpResult

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTotpResult from a JSON string
verify_totp_result_instance = VerifyTotpResult.from_json(json)
# print the JSON string representation of the object
print(VerifyTotpResult.to_json())

# convert the object into a dict
verify_totp_result_dict = verify_totp_result_instance.to_dict()
# create an instance of VerifyTotpResult from a dict
verify_totp_result_from_dict = VerifyTotpResult.from_dict(verify_totp_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


