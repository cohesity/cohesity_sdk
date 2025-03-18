# S3LifecycleManagement

Specifies the S3 Lifecycle policy of the bucket. If not specified no Lifecycle management is performed for objects in this bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[LifecycleRule]**](LifecycleRule.md) | Specifies Lifecycle configuration rules for an Amazon S3 bucket. A maximum of 1000 rules can be specified. | [optional] 
**version_id** | **int** | Specifies a unique monotonically increasing version for the lifecycle configuration. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.s3_lifecycle_management import S3LifecycleManagement

# TODO update the JSON string below
json = "{}"
# create an instance of S3LifecycleManagement from a JSON string
s3_lifecycle_management_instance = S3LifecycleManagement.from_json(json)
# print the JSON string representation of the object
print(S3LifecycleManagement.to_json())

# convert the object into a dict
s3_lifecycle_management_dict = s3_lifecycle_management_instance.to_dict()
# create an instance of S3LifecycleManagement from a dict
s3_lifecycle_management_from_dict = S3LifecycleManagement.from_dict(s3_lifecycle_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


