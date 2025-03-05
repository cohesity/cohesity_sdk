# AntivirusService

Specifies an Antivirus Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the description for the Antivirus Service. | [optional] 
**icap_uri** | **str** | Specifies the ICAP Uri for the Antivirus Service. | 
**tag** | **str** | Specifies the tag of the Antivirus Service. | [optional] [readonly] 
**tag_id** | **int** | Specifies the tag id of the Antivirus Service. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.antivirus_service import AntivirusService

# TODO update the JSON string below
json = "{}"
# create an instance of AntivirusService from a JSON string
antivirus_service_instance = AntivirusService.from_json(json)
# print the JSON string representation of the object
print(AntivirusService.to_json())

# convert the object into a dict
antivirus_service_dict = antivirus_service_instance.to_dict()
# create an instance of AntivirusService from a dict
antivirus_service_from_dict = AntivirusService.from_dict(antivirus_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


