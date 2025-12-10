# RecoverGCPBigQueryParams

Specifies the parameters to recover GCP BigQuery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPBigQuery**](GCPTargetParamsForRecoverGCPBigQuery.md) |  | 
**snapshots** | [**List[RecoverGCPBigQuerySnapshotParams]**](RecoverGCPBigQuerySnapshotParams.md) | Specifies the details of the gcp bigquery objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_big_query_params import RecoverGCPBigQueryParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPBigQueryParams from a JSON string
recover_gcp_big_query_params_instance = RecoverGCPBigQueryParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPBigQueryParams.to_json())

# convert the object into a dict
recover_gcp_big_query_params_dict = recover_gcp_big_query_params_instance.to_dict()
# create an instance of RecoverGCPBigQueryParams from a dict
recover_gcp_big_query_params_from_dict = RecoverGCPBigQueryParams.from_dict(recover_gcp_big_query_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


