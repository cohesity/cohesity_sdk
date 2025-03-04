# S3AccountParams

Specifies S3 Account parameters for User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_access_key_id** | **str** | Specifies the S3 Account Access Key ID. | [optional] 
**s3_account_id** | **str** | Specifies the S3 Account Canonical User ID. | [optional] 
**s3_secret_key** | **str** | Specifies the S3 Account Secret Key. | [optional] 

## Example

```python
from cohesity_sdk.models.s3_account_params import S3AccountParams

# TODO update the JSON string below
json = "{}"
# create an instance of S3AccountParams from a JSON string
s3_account_params_instance = S3AccountParams.from_json(json)
# print the JSON string representation of the object
print(S3AccountParams.to_json())

# convert the object into a dict
s3_account_params_dict = s3_account_params_instance.to_dict()
# create an instance of S3AccountParams from a dict
s3_account_params_from_dict = S3AccountParams.from_dict(s3_account_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


