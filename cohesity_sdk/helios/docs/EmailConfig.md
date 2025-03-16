# EmailConfig

Specifies the email config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cc** | **List[str]** | Carbon copy recepient email addresses. | [optional] 
**options** | [**List[ConfigItem]**](ConfigItem.md) | Optional configuration. | [optional] 
**to** | **List[str]** | Main recepient email addresses. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.email_config import EmailConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfig from a JSON string
email_config_instance = EmailConfig.from_json(json)
# print the JSON string representation of the object
print(EmailConfig.to_json())

# convert the object into a dict
email_config_dict = email_config_instance.to_dict()
# create an instance of EmailConfig from a dict
email_config_from_dict = EmailConfig.from_dict(email_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


