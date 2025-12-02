# S3Keys

Specifies the S3 Access keys for a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_access_key_id** | **str** | Specifies the S3 Account Access Key ID. Allowed characters are: AlphaNumeric(a-zA-z0-9), underscore(_) and hyphen(-). Key should contain exactly 43 characters. | [optional] 
**s3_secret_key** | **str** | Specifies the S3 Account Secret Key. Allowed characters are: AlphaNumeric(a-zA-z0-9), underscore(_) and hyphen(-). Key should contain exactly 43 characters. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.s3_keys import S3Keys

# TODO update the JSON string below
json = "{}"
# create an instance of S3Keys from a JSON string
s3_keys_instance = S3Keys.from_json(json)
# print the JSON string representation of the object
print(S3Keys.to_json())

# convert the object into a dict
s3_keys_dict = s3_keys_instance.to_dict()
# create an instance of S3Keys from a dict
s3_keys_from_dict = S3Keys.from_dict(s3_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


