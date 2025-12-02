# LoginBanner

Stores login banner information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Specifies the content of the banner. | 
**is_enabled** | **bool** | Specifies banner state is enabled or disabled. Default value for this field is true. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.login_banner import LoginBanner

# TODO update the JSON string below
json = "{}"
# create an instance of LoginBanner from a JSON string
login_banner_instance = LoginBanner.from_json(json)
# print the JSON string representation of the object
print(LoginBanner.to_json())

# convert the object into a dict
login_banner_dict = login_banner_instance.to_dict()
# create an instance of LoginBanner from a dict
login_banner_from_dict = LoginBanner.from_dict(login_banner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


