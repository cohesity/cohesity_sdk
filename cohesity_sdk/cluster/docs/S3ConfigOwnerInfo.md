# S3ConfigOwnerInfo

Specifies the owner info of the View as an S3 bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguished_name** | **str** | Specifies the distinguished name of the bucket owner for an ABAC enabled S3 Bucket. | [optional] 
**user_id** | **str** | Specifies the user id of the owner. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.s3_config_owner_info import S3ConfigOwnerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of S3ConfigOwnerInfo from a JSON string
s3_config_owner_info_instance = S3ConfigOwnerInfo.from_json(json)
# print the JSON string representation of the object
print(S3ConfigOwnerInfo.to_json())

# convert the object into a dict
s3_config_owner_info_dict = s3_config_owner_info_instance.to_dict()
# create an instance of S3ConfigOwnerInfo from a dict
s3_config_owner_info_from_dict = S3ConfigOwnerInfo.from_dict(s3_config_owner_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


