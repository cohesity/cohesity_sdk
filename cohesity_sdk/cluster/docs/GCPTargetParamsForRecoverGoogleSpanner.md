# GCPTargetParamsForRecoverGoogleSpanner

Specifies the recovery target params for Google Spanner target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for Spanner recovery. | [optional] 
**max_workers** | **int** | Maximum number of Dataflow workers to use (cost limiter). | [default to 10]
**new_source_config** | [**RecoverGoogleSpannerNewSourceConfig**](RecoverGoogleSpannerNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**vpc_network** | **str** | VPC network name for Dataflow processing. | 
**vpc_subnet** | **str** | Subnet name within the VPC for Dataflow processing. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_google_spanner import GCPTargetParamsForRecoverGoogleSpanner

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTargetParamsForRecoverGoogleSpanner from a JSON string
gcp_target_params_for_recover_google_spanner_instance = GCPTargetParamsForRecoverGoogleSpanner.from_json(json)
# print the JSON string representation of the object
print(GCPTargetParamsForRecoverGoogleSpanner.to_json())

# convert the object into a dict
gcp_target_params_for_recover_google_spanner_dict = gcp_target_params_for_recover_google_spanner_instance.to_dict()
# create an instance of GCPTargetParamsForRecoverGoogleSpanner from a dict
gcp_target_params_for_recover_google_spanner_from_dict = GCPTargetParamsForRecoverGoogleSpanner.from_dict(gcp_target_params_for_recover_google_spanner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


