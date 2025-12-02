# RecoverGoogleSpannerNewSourceConfig

Specifies the configuration for recovering Google Spanner database to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**target_instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_google_spanner_new_source_config import RecoverGoogleSpannerNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGoogleSpannerNewSourceConfig from a JSON string
recover_google_spanner_new_source_config_instance = RecoverGoogleSpannerNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGoogleSpannerNewSourceConfig.to_json())

# convert the object into a dict
recover_google_spanner_new_source_config_dict = recover_google_spanner_new_source_config_instance.to_dict()
# create an instance of RecoverGoogleSpannerNewSourceConfig from a dict
recover_google_spanner_new_source_config_from_dict = RecoverGoogleSpannerNewSourceConfig.from_dict(recover_google_spanner_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


