# BigQueryProtectionGroupObjectParams

Specifies the object parameters to create GCP BigQuery Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the dataset. | 
**name** | **str** | Specifies the name of the dataset. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.big_query_protection_group_object_params import BigQueryProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryProtectionGroupObjectParams from a JSON string
big_query_protection_group_object_params_instance = BigQueryProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(BigQueryProtectionGroupObjectParams.to_json())

# convert the object into a dict
big_query_protection_group_object_params_dict = big_query_protection_group_object_params_instance.to_dict()
# create an instance of BigQueryProtectionGroupObjectParams from a dict
big_query_protection_group_object_params_from_dict = BigQueryProtectionGroupObjectParams.from_dict(big_query_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


