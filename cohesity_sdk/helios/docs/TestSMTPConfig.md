# TestSMTPConfig

Specifies a request body to send a test email and validate SMTP configuration. Ensure SMTP is configured on the cluster and that it is not disabled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Specifies the recipient&#39;s email address. | 

## Example

```python
from cohesity_sdk.helios.models.test_smtp_config import TestSMTPConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TestSMTPConfig from a JSON string
test_smtp_config_instance = TestSMTPConfig.from_json(json)
# print the JSON string representation of the object
print(TestSMTPConfig.to_json())

# convert the object into a dict
test_smtp_config_dict = test_smtp_config_instance.to_dict()
# create an instance of TestSMTPConfig from a dict
test_smtp_config_from_dict = TestSMTPConfig.from_dict(test_smtp_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


