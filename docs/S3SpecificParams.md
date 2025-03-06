# S3SpecificParams

Specifies the s3 specific parameters for source registration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_report_bucket** | **str** | Specifies the ARN for S3 bucket where inventory reports are to be stored. | 
**inventory_report_prefix** | **str** | The inventory bucket prefix where inventory reports are to be stored. | 

## Example

```python
from cohesity_sdk.cluster.models.s3_specific_params import S3SpecificParams

# TODO update the JSON string below
json = "{}"
# create an instance of S3SpecificParams from a JSON string
s3_specific_params_instance = S3SpecificParams.from_json(json)
# print the JSON string representation of the object
print(S3SpecificParams.to_json())

# convert the object into a dict
s3_specific_params_dict = s3_specific_params_instance.to_dict()
# create an instance of S3SpecificParams from a dict
s3_specific_params_from_dict = S3SpecificParams.from_dict(s3_specific_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


