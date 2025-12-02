# CohesionHeliosConnectionInfo

Specifies the Cohesion Helios connection information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Specifies if the connection is active. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cohesion_helios_connection_info import CohesionHeliosConnectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CohesionHeliosConnectionInfo from a JSON string
cohesion_helios_connection_info_instance = CohesionHeliosConnectionInfo.from_json(json)
# print the JSON string representation of the object
print(CohesionHeliosConnectionInfo.to_json())

# convert the object into a dict
cohesion_helios_connection_info_dict = cohesion_helios_connection_info_instance.to_dict()
# create an instance of CohesionHeliosConnectionInfo from a dict
cohesion_helios_connection_info_from_dict = CohesionHeliosConnectionInfo.from_dict(cohesion_helios_connection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


