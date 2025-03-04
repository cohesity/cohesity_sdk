# VcdConnectionParams

Specifies the parameters to connect to a seed node and fetch information from its config file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**host** | **str** | IP or hostname of the source. | 

## Example

```python
from cohesity_sdk.models.vcd_connection_params import VcdConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of VcdConnectionParams from a JSON string
vcd_connection_params_instance = VcdConnectionParams.from_json(json)
# print the JSON string representation of the object
print(VcdConnectionParams.to_json())

# convert the object into a dict
vcd_connection_params_dict = vcd_connection_params_instance.to_dict()
# create an instance of VcdConnectionParams from a dict
vcd_connection_params_from_dict = VcdConnectionParams.from_dict(vcd_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


