# SpannerProtectionGroupParams

Specifies the parameters which are specific to Google Spanner related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_data_boost** | **bool** | Enables Spanner Data Boost to minimize impact on OLTP workloads. | [optional] [default to True]
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**export_bucket_name** | **str** | The Google Cloud Storage bucket name for Spanner export. | [optional] 
**max_workers** | **int** | Maximum number of Dataflow workers to use (cost limiter). | [optional] 
**objects** | [**List[SpannerProtectionGroupObjectParams]**](SpannerProtectionGroupObjectParams.md) | Specifies the Spanner databases to be included in the Protection Group. | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 
**vpc_network** | **str** | VPC network name for Dataflow processing. | 
**vpc_subnet** | **str** | Subnet name within the VPC for Dataflow processing. | 

## Example

```python
from cohesity_sdk.cluster.models.spanner_protection_group_params import SpannerProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of SpannerProtectionGroupParams from a JSON string
spanner_protection_group_params_instance = SpannerProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(SpannerProtectionGroupParams.to_json())

# convert the object into a dict
spanner_protection_group_params_dict = spanner_protection_group_params_instance.to_dict()
# create an instance of SpannerProtectionGroupParams from a dict
spanner_protection_group_params_from_dict = SpannerProtectionGroupParams.from_dict(spanner_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


