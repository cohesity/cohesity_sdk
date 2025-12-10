# RecoverGoogleSpannerParams

Specifies the parameters to recover Google Spanner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGoogleSpanner**](GCPTargetParamsForRecoverGoogleSpanner.md) |  | 
**snapshots** | [**List[RecoverGoogleSpannerSnapshotParams]**](RecoverGoogleSpannerSnapshotParams.md) | Specifies the details of the gcp spanner objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_google_spanner_params import RecoverGoogleSpannerParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGoogleSpannerParams from a JSON string
recover_google_spanner_params_instance = RecoverGoogleSpannerParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGoogleSpannerParams.to_json())

# convert the object into a dict
recover_google_spanner_params_dict = recover_google_spanner_params_instance.to_dict()
# create an instance of RecoverGoogleSpannerParams from a dict
recover_google_spanner_params_from_dict = RecoverGoogleSpannerParams.from_dict(recover_google_spanner_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


