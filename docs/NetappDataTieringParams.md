# NetappDataTieringParams

Specifies the parameters which are specific to Netapp related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[ProtectionObjectInput]**](ProtectionObjectInput.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the root of data tiering source. | [optional] 

## Example

```python
from cohesity_sdk.models.netapp_data_tiering_params import NetappDataTieringParams

# TODO update the JSON string below
json = "{}"
# create an instance of NetappDataTieringParams from a JSON string
netapp_data_tiering_params_instance = NetappDataTieringParams.from_json(json)
# print the JSON string representation of the object
print(NetappDataTieringParams.to_json())

# convert the object into a dict
netapp_data_tiering_params_dict = netapp_data_tiering_params_instance.to_dict()
# create an instance of NetappDataTieringParams from a dict
netapp_data_tiering_params_from_dict = NetappDataTieringParams.from_dict(netapp_data_tiering_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


