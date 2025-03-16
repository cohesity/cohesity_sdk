# SMTPConfiguration

Specifies the SMTP configuration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Specifies the IP address or the FQDN of the SMTP server. | 
**is_active** | **bool** | Specifies if the SMTP configuration is active. | [optional] [default to True]
**port** | **int** | Specifies the SMTP port. Usually 465 or 587. For authenticated connection, it is generally 587. | 
**use_ssl** | **bool** | This is set to true when the SMTP server uses SSL/TLS without supporting STARTTLS. Typically, this is used for port 465. | [optional] [default to False]
**username** | **str** | Specifies the username which will be used to connect to the SMTP server. If username is not specified, then it would imply that SMTP server is set up for unauthenticated access. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.smtp_configuration import SMTPConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SMTPConfiguration from a JSON string
smtp_configuration_instance = SMTPConfiguration.from_json(json)
# print the JSON string representation of the object
print(SMTPConfiguration.to_json())

# convert the object into a dict
smtp_configuration_dict = smtp_configuration_instance.to_dict()
# create an instance of SMTPConfiguration from a dict
smtp_configuration_from_dict = SMTPConfiguration.from_dict(smtp_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


