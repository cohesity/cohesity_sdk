# GCPTargetParamsForRecoverGCPBigQuery

Specifies the recovery target params for GCP BigQuery target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_auto_create** | **bool** | Specifies whether to auto create the Cloud Storage bucket if it does not exist. | [optional] 
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for BigQuery recovery. | [optional] 
**new_source_config** | [**RecoverGCPBigQueryNewSourceConfig**](RecoverGCPBigQueryNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_gcp_big_query import GCPTargetParamsForRecoverGCPBigQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTargetParamsForRecoverGCPBigQuery from a JSON string
gcp_target_params_for_recover_gcp_big_query_instance = GCPTargetParamsForRecoverGCPBigQuery.from_json(json)
# print the JSON string representation of the object
print(GCPTargetParamsForRecoverGCPBigQuery.to_json())

# convert the object into a dict
gcp_target_params_for_recover_gcp_big_query_dict = gcp_target_params_for_recover_gcp_big_query_instance.to_dict()
# create an instance of GCPTargetParamsForRecoverGCPBigQuery from a dict
gcp_target_params_for_recover_gcp_big_query_from_dict = GCPTargetParamsForRecoverGCPBigQuery.from_dict(gcp_target_params_for_recover_gcp_big_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


