# BigQueryProtectionGroupParams

Specifies the parameters which are specific to GCP BigQuery related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | Specifies whether to auto create the Cloud Storage bucket if it doesn&#39;t exist. | [optional] 
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for BigQuery backup. | 
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**List[BigQueryProtectionGroupObjectParams]**](BigQueryProtectionGroupObjectParams.md) | Specifies the BigQuery datasets to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.big_query_protection_group_params import BigQueryProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryProtectionGroupParams from a JSON string
big_query_protection_group_params_instance = BigQueryProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(BigQueryProtectionGroupParams.to_json())

# convert the object into a dict
big_query_protection_group_params_dict = big_query_protection_group_params_instance.to_dict()
# create an instance of BigQueryProtectionGroupParams from a dict
big_query_protection_group_params_from_dict = BigQueryProtectionGroupParams.from_dict(big_query_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


