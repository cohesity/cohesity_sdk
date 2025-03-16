# CommonAWSCategoryParams

Specifies the cloud category parameter which are specific to AWS related External Targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_type** | **str** | Specifies the AWS External Target type. | 

## Example

```python
from cohesity_sdk.helios.models.common_aws_category_params import CommonAWSCategoryParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonAWSCategoryParams from a JSON string
common_aws_category_params_instance = CommonAWSCategoryParams.from_json(json)
# print the JSON string representation of the object
print(CommonAWSCategoryParams.to_json())

# convert the object into a dict
common_aws_category_params_dict = common_aws_category_params_instance.to_dict()
# create an instance of CommonAWSCategoryParams from a dict
common_aws_category_params_from_dict = CommonAWSCategoryParams.from_dict(common_aws_category_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


