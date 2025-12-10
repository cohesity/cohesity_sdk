# AwsRedshiftProtectionGroupObjectParams

Specifies the object parameters to create an Redshift Ingest Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the object. | 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.aws_redshift_protection_group_object_params import AwsRedshiftProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRedshiftProtectionGroupObjectParams from a JSON string
aws_redshift_protection_group_object_params_instance = AwsRedshiftProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(AwsRedshiftProtectionGroupObjectParams.to_json())

# convert the object into a dict
aws_redshift_protection_group_object_params_dict = aws_redshift_protection_group_object_params_instance.to_dict()
# create an instance of AwsRedshiftProtectionGroupObjectParams from a dict
aws_redshift_protection_group_object_params_from_dict = AwsRedshiftProtectionGroupObjectParams.from_dict(aws_redshift_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


