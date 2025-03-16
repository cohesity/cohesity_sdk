# LifecycleRule

Specifies the Lifecycle configuration rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_incomplete_multipart_upload_action** | [**AbortIncompleteMultipartUploadAction**](AbortIncompleteMultipartUploadAction.md) | Specifies the days since the initiation of an incomplete multipart upload before permanently removing all parts of the upload. | [optional] 
**expiration** | [**ExpirationAction**](ExpirationAction.md) | Specifies the expiration for the lifecycle of the object in the form of date, days and whether the object has a delete marker. | [optional] 
**filter** | [**LifecycleRuleFilter**](LifecycleRuleFilter.md) | Specifies the filter used to identify objects that a Lifecycle Rule applies to. | [optional] 
**id** | **str** | Specifies the Unique identifier for the rule. The value cannot be longer than 255 characters. | 
**non_current_version_expiration_action** | [**NonCurrentVersionExpirationAction**](NonCurrentVersionExpirationAction.md) | Specifies when non-current object versions expire. Upon expiration, non-current object versions are permanently deleted. The action can be specified only in versioning enabled or suspended buckets. | [optional] 
**prefix** | **str** | Specifies the prefix used to identify objects that a lifecycle rule applies to. | [optional] 
**status** | **bool** | Specifies if the rule is currently being applied. | 

## Example

```python
from cohesity_sdk.helios.models.lifecycle_rule import LifecycleRule

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleRule from a JSON string
lifecycle_rule_instance = LifecycleRule.from_json(json)
# print the JSON string representation of the object
print(LifecycleRule.to_json())

# convert the object into a dict
lifecycle_rule_dict = lifecycle_rule_instance.to_dict()
# create an instance of LifecycleRule from a dict
lifecycle_rule_from_dict = LifecycleRule.from_dict(lifecycle_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


