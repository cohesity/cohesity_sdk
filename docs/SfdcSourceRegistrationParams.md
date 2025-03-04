# SfdcSourceRegistrationParams

Specifies parameters to register an SFDC Protection Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** | Specifies the token that will be used for fetching oAuth tokens from salesforce. | 
**callback_url** | **str** | Specifies the URL added in the connected apps Callback URL field. You can find this URL on the connected apps Manage Connected Apps page or from the connected apps definition. This value must be URL encoded. | [optional] 
**concurrent_api_requests_limit** | **int** | Specifies the maximum number of concurrent API requests allowed for salesforce. | 
**consumer_key** | **str** | Specifies Consumer key from the connected app in SFDC. | 
**consumer_secret** | **str** | Specifies Consumer secret from the connected app in SFDC. | 
**daily_api_limit** | **int** | Specifies the maximum number of daily API requests allowed for salesforce. | 
**endpoint** | **str** | Specifies the SFDC endpoint URL. | 
**endpoint_type** | **str** | SFDC Endpoint type. | 
**metadata_endpoint_url** | **str** | Specifies the url to access salesforce metadata requests. | [optional] [readonly] 
**password** | **str** | Specifies the password to access salesforce. | [optional] 
**soap_endpoint_url** | **str** | Specifies the url to access salesforce soap requests. | [optional] [readonly] 
**username** | **str** | Specifies the username to access salesforce. | [optional] 

## Example

```python
from cohesity_sdk.models.sfdc_source_registration_params import SfdcSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of SfdcSourceRegistrationParams from a JSON string
sfdc_source_registration_params_instance = SfdcSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(SfdcSourceRegistrationParams.to_json())

# convert the object into a dict
sfdc_source_registration_params_dict = sfdc_source_registration_params_instance.to_dict()
# create an instance of SfdcSourceRegistrationParams from a dict
sfdc_source_registration_params_from_dict = SfdcSourceRegistrationParams.from_dict(sfdc_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


