# UpdateSMTPParams

Specifies the parameters to update cluster SMTP configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Specifies the IP address or the FQDN of the SMTP server. | 
**is_active** | **bool** | Specifies if the SMTP configuration is active. | [optional] [default to True]
**port** | **int** | Specifies the SMTP port. Usually 465 or 587. For authenticated connection, it is generally 587. | 
**use_ssl** | **bool** | This is set to true when the SMTP server uses SSL/TLS without supporting STARTTLS. Typically, this is used for port 465. | [optional] [default to False]
**username** | **str** | Specifies the username which will be used to connect to the SMTP server. If username is not specified, then it would imply that SMTP server is set up for unauthenticated access. | [optional] 
**password** | **str** | Specifies the password of the SMTP user. This is required if username is specified in the request. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_smtp_params import UpdateSMTPParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSMTPParams from a JSON string
update_smtp_params_instance = UpdateSMTPParams.from_json(json)
# print the JSON string representation of the object
print(UpdateSMTPParams.to_json())

# convert the object into a dict
update_smtp_params_dict = update_smtp_params_instance.to_dict()
# create an instance of UpdateSMTPParams from a dict
update_smtp_params_from_dict = UpdateSMTPParams.from_dict(update_smtp_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


