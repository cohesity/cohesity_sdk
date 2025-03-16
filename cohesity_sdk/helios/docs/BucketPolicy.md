# BucketPolicy

Specifies the policy in effect for this bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the identifier of the bucket policy. This is a read-only property. | [optional] 
**raw_policy** | **str** | Specifies the raw JSON string of the store policy. | 
**version** | **str** | Specifies the language syntax rules that are to be used to process the policy. This is a read-only property. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.bucket_policy import BucketPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of BucketPolicy from a JSON string
bucket_policy_instance = BucketPolicy.from_json(json)
# print the JSON string representation of the object
print(BucketPolicy.to_json())

# convert the object into a dict
bucket_policy_dict = bucket_policy_instance.to_dict()
# create an instance of BucketPolicy from a dict
bucket_policy_from_dict = BucketPolicy.from_dict(bucket_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


