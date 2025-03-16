# OAuthAudience

OAuth 2 Audience

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience_id** | **str** | Specifies the ID of this audience. This must match the &#39;aud&#39; field in the token at login time. | 
**client_ids** | **List[str]** | Specifies the list of client IDs which should be allowed to log in via this audience. The &#39;appid&#39; in the token must match one of the values specified here. | 

## Example

```python
from cohesity_sdk.helios.models.o_auth_audience import OAuthAudience

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthAudience from a JSON string
o_auth_audience_instance = OAuthAudience.from_json(json)
# print the JSON string representation of the object
print(OAuthAudience.to_json())

# convert the object into a dict
o_auth_audience_dict = o_auth_audience_instance.to_dict()
# create an instance of OAuthAudience from a dict
o_auth_audience_from_dict = OAuthAudience.from_dict(o_auth_audience_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


