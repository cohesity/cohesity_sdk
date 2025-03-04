# HostInformation

Specifies the host information for a objects. This is mainly populated in case of App objects where app object is hosted by another object such as VM or physical server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **str** | Specifies the id of the host object. | [optional] 
**name** | **str** | Specifies the name of the host object. | [optional] 

## Example

```python
from cohesity_sdk.models.host_information import HostInformation

# TODO update the JSON string below
json = "{}"
# create an instance of HostInformation from a JSON string
host_information_instance = HostInformation.from_json(json)
# print the JSON string representation of the object
print(HostInformation.to_json())

# convert the object into a dict
host_information_dict = host_information_instance.to_dict()
# create an instance of HostInformation from a dict
host_information_from_dict = HostInformation.from_dict(host_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


